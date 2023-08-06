"""Classes to control communication with parallel subprocesses"""
import os
import sys
import signal
import psutil
import pickle
import time
import atexit
import threading
from subprocess import Popen, PIPE
from pathlib import Path
from queue import Queue
from ..utils.controlflags import ControlFlag

class WorkerDiedException(Exception):
    pass

class WorkerCrashed(Exception):
    """Indicates that a worker has crashed"""


def get_default_worker_script():
    """Get the default worker.py script"""
    # import dft_python_api.worker as worker_init_script
    # root_py = Path(os.path.realpath(worker_init_script.__file__))
    # return root_py.parent / 'worker.py'
    return "-mdft_python_api.worker.worker"

# Cleanup code
DEBUG_CLEANUP=False

def cleanup_process(process: psutil.Process):
    """Terminate process and all children (ie mpirun children)"""
    if DEBUG_CLEANUP:
        print("killing process", process)

    # Gather child pids to kill
    try:
        children = list(process.children(recursive=True))
    except psutil.NoSuchProcess:
        children = []

    try:
        process.kill()
    except psutil.NoSuchProcess:
        pass

    # Kill children (ie worker threads that may have a different pgid )
    for c in children:
        if DEBUG_CLEANUP:
            print("killing child", c)
        c.kill()
    
def cleanup_file(pipe_file):
    """Delete a file"""
    try:
        if DEBUG_CLEANUP:
            print("Removing pipe", pipe_file)
        os.remove(pipe_file)
    except FileNotFoundError:
        pass # Ignore if already deleted

class Worker:
    """Represents a collection of workers of variable sizes"""
    def __init__(self, name, max_cores, single_worker_mode=True, mpirun_command="mpirun", mpirun_flags=None):
        self.name = name
        self.max_cores = max_cores
        self.used_cores = 0
        self.current_worker_id = 0
        self.workers = dict()

        self.mpirun_command = mpirun_command
        if mpirun_flags is None:
            self.mpirun_flags = ["-np", "{num_cores}"]
        else:
            self.mpirun_flags = mpirun_flags

        self.work_queue = Queue()
        self.results_queue = Queue()

        if single_worker_mode:
            self.add_workers(max_cores)

    def add_workers(self, num_cores_per_worker, num_workers=1):
        """Add more workers to the worker pool"""
        if self.used_cores + num_workers * num_cores_per_worker > self.max_cores:
            raise ValueError("Attempted to spawn more worker threads than max_cores!")
        self.used_cores += num_workers * num_cores_per_worker

        for _ in range(num_workers):
            worker_id = f"{self.name}-{self.get_next_id()}"
            worker = WorkerIO(worker_id=worker_id,
                       num_cores=num_cores_per_worker,
                       work_queue=self.work_queue,
                       results_queue=self.results_queue,
                       mpirun_command=self.mpirun_command,
                       mpirun_flags=self.mpirun_flags
            )
            self.workers[worker_id] = worker

    def add_task(self, task_id, task):
        """Adds a task to the queue"""
        self.work_queue.put((task_id, task))

    def get_next_id(self):
        """Get the next free worker id"""
        self.current_worker_id += 1
        return self.current_worker_id


    def kill(self):
        """Kills all subprocesses"""
        for worker in self.workers.values():
            worker.kill()

    def finish(self):
        """Sends the polite finish message to all workers"""
        assert self.work_queue.empty(), "Work queue wasn't empty!"
        for worker in self.workers.values():
            worker.finish()

    def get_next_finished(self):
        """Return the next finished task"""
        return_value = self.results_queue.get()

        task_id, result, *error_info = return_value

        if result == ControlFlag.WORKER_CRASHED:
            error_task, worker_id = error_info
            if hasattr(error_task, "get_error"):
                err_msg = error_task.get_error(worker_id)
                raise WorkerDiedException(f"Worker died on task with message:\n{error_task}\n{err_msg}")
            else:
                raise WorkerDiedException(f"Worker died on task {task_id}")
        else:
            return task_id, result


    def get_next_result(self):
        """Return the next finished task which returns a result"""
        result = None
        while result is None:
            task_id, result = self.get_next_finished()
        return task_id, result

class WorkerIO:
    """Represents an individual worker"""
    def __init__(self, worker_id, num_cores, work_queue, results_queue, mpirun_command, mpirun_flags, worker_py=None):
        """Initialise a worker thread"""
        if worker_py is None:
            worker_py = get_default_worker_script()

        # Use current python executable
        py_exe = sys.executable

        self.num_cores = num_cores

        # We replace named entries in flags -- eg {num_cores} becomes the number of cores
        # TODO: Test this with other mpirun style things (srun etc)
        replacements = {
            "num_cores": str(num_cores)
            }

        mpi_flags = [f.format(**replacements) for f in mpirun_flags]

        self.process_cmd = mpirun_command, *mpi_flags, py_exe, str(worker_py)

        self.worker_id = worker_id
        self.work_queue = work_queue
        self.results_queue = results_queue

        # Start the process
        self.process = Popen(self.process_cmd, shell=False,
                             stdin=PIPE, bufsize=0)   # PIPE with no buffering

        # Immediately add to kill at exit list
        atexit.register(cleanup_process, psutil.Process(self.process.pid))

        # Make a named pipe for this process
        self.fname = f'.worker-{id(self)}-iopipe'
        os.mkfifo(self.fname, mode=0o777)
        atexit.register(cleanup_file, self.fname)
        
        # Send worker id and pipe name
        self.send(self.fname)           # Send pipe name
        self.send(self.worker_id)       # Send worker id

        # Now open pipe for reading
        self.pipe = open(self.fname, 'rb')

        # Go into work loop
        self.thread = threading.Thread(target=self.work_loop,
                                       name=f"worker-{worker_id}",
                                       daemon=True)
        self.thread.start()

    def work_loop(self):
        """Take items from work queue, process them and send results to result_queue"""
        while True:
            task_id, task = self.work_queue.get()
            try:
                self.send(task)
            except BrokenPipeError:
                print(f"Died sending data: {task_id, task}")
                self.results_queue.put((task_id, ControlFlag.WORKER_CRASHED, task, self.worker_id))
                break

            if task == ControlFlag.END:
                break

            try:
                result = self.read()
            except (BrokenPipeError, EOFError):
                print(f"Died while waiting on response for task: {task_id, task}")
                self.results_queue.put((task_id, ControlFlag.WORKER_CRASHED, task, self.worker_id))
                break

            self.results_queue.put((task_id, result))
            self.work_queue.task_done()



    def send(self, data: object):
        """Send object to child process"""
        pickle.dump(data, self.process.stdin)
        self.process.stdin.flush()

    def read(self) -> object:
        """Read object from child process synchronously"""
        return pickle.load(self.pipe)


    def __repr__(self):
        return "Worker(id={0.worker_id}, num_cores={0.num_cores})".format(self)


    def finish(self):
        """Polite message to thread and subprocess to close"""
        self.work_queue.put((-1, ControlFlag.END))

    def kill(self):
        """Send kill signal to subprocess"""

        # First enumerate children
        parent = psutil.Process(self.process.pid)
        children = list(parent.children(recursive=True))

        # Send kill to mpirun
        self.process.kill()

        # Kill children (ie worker threads that may have a different pgid )
        for c in children:
            c.kill()

        time.sleep(0.1)

        try:
            os.remove(self.fname)
        except FileNotFoundError:
            pass # Ignore if already deleted

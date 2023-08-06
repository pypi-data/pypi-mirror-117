#!/usr/bin/env python3
"""Main worker script that is run in parallel"""
import sys
import os
from mpi4py import MPI
from dft_python_api.utils.controlflags import ControlFlag
from dft_python_api.worker.worker_io import ParentIO
from dft_python_api.tasks.worker_environment import Envs
from dft_python_api.tasks.task import Task


def get_printfn(worker_id, rank, debug=True):
    """Returns a stderr print function with tags for process information"""
    def printfn(*args, **kw):
        """
        Print function that writes to stderr rather than stdout,
        as this is connected to the master process
        """
        print(f"<Worker {worker_id}.{rank}> ", end='')
        print(*args, **kw)
        sys.stdout.flush()

    def noprint(*args, **kw):
        pass

    if debug:
        return printfn
    else:
        return noprint


def worker_main():
    """
    This is the main loop for a parallel worker.
    """
    # Get some MPI parameters
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    on_root = rank == 0

    # Create a reader/writer to the main process
    parent_io = ParentIO(comm)

    # Read worker id and debug level
    worker_id = parent_io.recv_all()

    # Generate pretty printer
    printfn = get_printfn(worker_id, rank, debug=False)

    # Create empty environments set
    envs = Envs(worker_id, on_root)

    while True:

        # Receive data from master
        task = parent_io.recv_all()
        results = None

        # Check if the data is an end signal
        if task == ControlFlag.END:
            break
        if task is ControlFlag.CRASH:
            if on_root:
                printfn("Crashing on command....")
                comm.Abort()
        elif isinstance(task, Task):
            printfn(f'Running task: {task}')
            task.run(envs, comm)
            results = task.results
            if results:
                printfn(f"Finished. Results: {results}")
            else:
                printfn(f"Finished.")
        else:
            printfn("Unknown object recieved?")
            comm.Abort()


        #Send data back to master
        parent_io.send(results)


if __name__ == "__main__":
    worker_main()

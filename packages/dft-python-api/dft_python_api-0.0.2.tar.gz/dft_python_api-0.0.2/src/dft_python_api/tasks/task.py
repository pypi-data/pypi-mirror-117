"""Module defining a Task and a wrapper to say what environment we want to run it in."""
from functools import wraps

def requires_env(envtype: type):
    """Wrapper that forces the required environment to be loaded"""
    def env_wrapper(func):
        @wraps(func)
        def wrapped_func(environments, mpi_comm, *args, **kwargs):
            environments.get_env(envtype, mpi_comm) # Needs comm for barrier sync
            return func(mpi_comm, *args, **kwargs)
        return wrapped_func
    return env_wrapper

class Task:
    """This is a class to act as a task for the worker to do."""
    def __init__(self, task_fn, *args, **kwargs):
        """Creates a task object that can be created on the master and executed by the workers"""
        self.task = task_fn
        self.args = args
        self.kwargs = kwargs
        self.results = None

    def run(self, environments, mpi_comm):
        """Run the task (to be called on the worker)"""
        self.results = self.task(environments, mpi_comm, *self.args, **self.kwargs)

    def __repr__(self):
        repr_str = f"TaskType: {type(self).__name__} Task: {self.task.__name__}"
        if self.args:    
            repr_str += f"\n\tDataArgs: {self.args}"
        if self.kwargs:  
            repr_str += f"\n\tDataKWargs: {self.kwargs}"
        return repr_str

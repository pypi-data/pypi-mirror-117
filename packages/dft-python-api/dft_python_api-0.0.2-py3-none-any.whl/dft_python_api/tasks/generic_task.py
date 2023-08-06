"""Example of simple generic tasks"""
#pylint: disable=unused-argument
from task import Task, requires_env
from worker_environment import Env

class GenericEnv(Env):
    """Example of a generic env that is just an empty folder"""
    def setup(self):
        self.id_name = "generic"


class GenericTask(Task):
    """Example of a generic task type"""

    @staticmethod                # Define as a static method (doesn't receive self)
    @requires_env(GenericEnv)    # Decorator to say we want to be in GenericEnv to run this
    def return_zero(mpi_comm):
        """Task that does nothing but return 0. Shows how task functions can be implemented"""
        return 0                 # Return the result that you want to send back to master

    @staticmethod
    @requires_env(GenericEnv)
    def add(mpi_comm, val1, val2):
        """Task that adds two numbers"""
        return val1 + val2

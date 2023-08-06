"""Module containing CASTEP specific task information"""
#pylint: disable=import-outside-toplevel, no-self-argument
from pathlib import Path
import sys
import numpy as np
import ase.io
from ..tasks.task import Task, requires_env
from ..tasks.worker_environment import Env
from ..utils.results import Results
from ..utils import units

# Make sure fortran files can be found... hacky
file = Path(__file__).resolve()
fortran_dir = file.parent / 'fortran_test_example'
sys.path.append(str(fortran_dir))


class FortEnv(Env):
    """Get a folder to run this instance in"""
    def setup(self):
        self.id_name = "fortran_test"

class FortTask(Task):
    """Fortran task example linking to code in fortan_test_example"""

    @staticmethod
    @requires_env(FortEnv)
    def add(mpi_comm, a, b):

        # Import the fortran module "fortran_test"
        # from the library file "fortran_code"
        from fortran_code import fortran_test # type: ignore

        # Fortran library call
        added_values = fortran_test.add_fort(a, b)

        # Return the result
        return added_values

    @staticmethod
    @requires_env(FortEnv)
    def comm_info(mpi_comm):
        # Import the fortran module "fortran_test"
        # from the library file "fortran_code"
        from fortran_code import fortran_test # type: ignore


        # Fortran library call (using mpi comm handle for fortran)
        comm_size = fortran_test.comm_info_fort(mpi_comm.py2f())

        # Return the result
        return comm_size
        

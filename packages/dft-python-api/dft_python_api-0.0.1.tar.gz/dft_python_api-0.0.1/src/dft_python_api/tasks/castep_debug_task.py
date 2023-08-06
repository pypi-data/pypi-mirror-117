"""Module containing CASTEP specific task information"""
#pylint: disable=import-outside-toplevel, no-self-argument
from pathlib import Path
import sys
import os
import numpy as np
from ase import Atoms
import ase.io
from .task import Task, requires_env
from .worker_environment import Env
from ..utils.results import Results
from ..utils import units

ATOMS = {}
PARAMS = {}
RESULTS = {}
SEEDNAME = "run"

class CastepDebugEnv(Env):
    """Get a folder to run this instance of CASTEP in"""
    def setup(self):
        self.id_name = "castep-debug"


def write_dict(filename, options):
    """Write options to file"""
    with open(filename, "w") as file_handle:
        for key, val in options.items():
            file_handle.write(f"{key} : {val}\n")


class CastepDebugTask(Task):
    """CASTEP specific tasks -- This version runs in serial by launching the executable manually"""

    @staticmethod 
    def get_default_parameters(task, atoms, **extra_args):
        """Return a default set of parameters for this task -- can be called on master"""
        if task in ["energy", "singlepoint", "SPE", "forces"]:
            params = {
                "cutoff_energy": "400 eV",
                "task": "SPE"
            }
        elif task in ['geometry']:
            params = {
                "cutoff_energy": "400 eV",
                "task": "geometryoptimisation"
            }
        else:
            raise ValueError("Invalid value for task: {}".format(task))

        # Now use the override values the user provided
        params.update(extra_args)
        return params

    @staticmethod
    @requires_env(CastepDebugEnv)
    def init(mpi_comm, atoms, params):
        """Initialise the cell and parameter data -- also initialise DFT code here if possible"""
        global ATOMS, PARAMS
        ATOMS = atoms
        PARAMS = params

    @staticmethod
    @requires_env(CastepDebugEnv)
    def finalise(mpi_comm):
        """Delete any static variables -- also call code cleanup methods here"""
        global ATOMS, PARAMS, RESULTS
        ATOMS = {}
        PARAMS = {}
        RESULTS = {}

    @staticmethod
    @requires_env(CastepDebugEnv)
    def update_params(mpi_comm, new_params):
        """Update the parameters set"""
        # Do some validation checking here
        pass

        # Now update the saved params
        PARAMS.update(new_params)

    @staticmethod
    @requires_env(CastepDebugEnv)
    def update_atoms(mpi_comm, new_atoms):
        """Update the atoms list"""
        global ATOMS

        # Optional validation checking
        pass

        # Now update saved atoms
        ATOMS = new_atoms

    @staticmethod
    @requires_env(CastepDebugEnv)
    def calculate(mpi_comm):
        """Do the actual calculation using the saved params and atoms"""
        global RESULTS

        param_file = f"{SEEDNAME}.param"
        cell_file = f"{SEEDNAME}.cell"

        if mpi_comm.Get_rank() == 0:
            # Write cell with ASE
            ase.io.write(cell_file,ATOMS)

            # Write params file
            write_dict(param_file, PARAMS)

        # Now run the actual code
        if mpi_comm.Get_rank() == 0:

            # Hacky way to launch mpirun version of process
            import subprocess
            from ase.calculators.castep import Castep

            castep_ase = Castep(directory=".", label=SEEDNAME)
            castep_filename = f"{SEEDNAME}.castep"
            if os.path.exists(castep_filename):
                os.remove(castep_filename)

            process_cmd = "castep.serial", SEEDNAME
            process = subprocess.run(process_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            #print(process.stdout, file=sys.stderr)
            #print(process.stderr, file=sys.stderr)
            #print("test:", process, file=sys.stderr)

            # Use ASE to read back in the .castep file
            castep_ase.read(f"{SEEDNAME}.castep")
            #def do_nothing(*args, **kwargs):
            #    pass

            #castep_ase.update = do_nothing

            energy = castep_ase._energy_free * units.eV
            forces = np.array(castep_ase._forces) * units.eV / units.angstrom

            # Set results
            RESULTS = Results(energy, forces)


        # Broadcast results to all nodes and return
        mpi_comm.bcast(RESULTS)
        return RESULTS

    @staticmethod
    @requires_env(CastepDebugEnv)
    def get_results(mpi_comm):
        return RESULTS

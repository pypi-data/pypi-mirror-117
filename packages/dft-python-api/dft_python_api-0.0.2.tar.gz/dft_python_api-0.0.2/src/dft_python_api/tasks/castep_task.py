"""Module containing CASTEP specific task information"""
#pylint: disable=import-outside-toplevel, no-self-argument
from pathlib import Path
import sys
import numpy as np
import ase.io
from ..utils import units
from ..tasks.task import Task, requires_env
from ..tasks.worker_environment import Env
from ..utils.results import Results
import glob

ATOMS = {}
PARAMS = {}
RESULTS = {}

SEEDNAME = 'run'

class CastepEnv(Env):
    """Get a folder to run this instance of CASTEP in"""
    def setup(self):
        self.id_name = "castep"


def write_dict(filename, options):
    """Write options to file"""
    with open(filename, "w") as file_handle:
        for key, val in options.items():
            file_handle.write(f"{key} : {val}\n")


class write_helper():
    def __init__(self, atoms):
        self.atoms = atoms


    # Copied from ASE Castep calculator -- required for cell writing
    def _get_number_in_species(self, at, atoms=None):
        """Return the number of the atoms within the set of it own
        species. If you are an ASE commiter: why not move this into
        ase.atoms.Atoms ?"""
        if atoms is None:
            atoms = self.atoms
        numbers = atoms.get_atomic_numbers()
        n = numbers[at]
        nis = numbers.tolist()[:at + 1].count(n)
        return nis

    def _get_absolute_number(self, species, nic, atoms=None):
        """This is the inverse function to _get_number in species."""
        if atoms is None:
            atoms = self.atoms
        ch = atoms.get_chemical_symbols()
        ch.reverse()
        total_nr = 0
        assert nic > 0, 'Number in species needs to be 1 or larger'
        while True:
            if ch.pop() == species:
                if nic == 1:
                    return total_nr
                nic -= 1
            total_nr += 1

class CastepTask(Task):
    """CASTEP specific tasks"""

    @staticmethod
    def get_error(worker_id):
        """Try and get the .err file"""
        err_files = glob.glob(f"./work/worker-{worker_id}-castep/*.err")
        if not err_files:
            return "No error file available"
        with open(err_files[0]) as err_file:
            err_msg = err_file.read()
        return err_msg

    @staticmethod
    def get_default_parameters(task, atoms=None, **extra_args):
        """
        Sets the default parameters object that we want. Override arguments with extra_args.
        This function is special and does not require a communicator and should be called by
        the main script.
        TODO: Maybe add a quality setting?
        """
        # Set the default parameters
        params = {
            "write_checkpoint": "None",
            "cutoff_energy": "200 eV",
            "opt_strategy": "speed"
        }

        if task in ["energy", "singlepoint", "SPE", "forces"]:
            params["task"] = "SPE"
        elif task in ['geometry']:
            params["task"] = "geometryoptimisation"

        else:
            raise ValueError("Invalid value for task: {}".format(task))

        # Add extra ones passed in
        params.update(extra_args)

        #Return the parameters object
        return params

    @staticmethod
    @requires_env(CastepEnv)
    def init(mpi_comm, atoms, params):
        """Initialise the DFT code"""
        from castep_python import Castep_Python
        global ATOMS, PARAMS
        ATOMS = atoms
        PARAMS = params

        # Write cell and param file for now
        param_file = f"{SEEDNAME}.param"
        cell_file = f"{SEEDNAME}.cell"

        # Write cell with ASE
        atoms.calc = write_helper(atoms)  # Hack to make cell contraints work
        ase.io.write(cell_file, ATOMS)

        # Write params file
        write_dict(param_file, PARAMS)

        # Do castep internal init
        Castep_Python.initialise(mpi_comm.py2f(), SEEDNAME)


    @staticmethod
    @requires_env(CastepEnv)
    def finalise(mpi_comm):
        """Delete any static variables -- also call code cleanup methods here"""
        from castep_python import Castep_Python
        global ATOMS, PARAMS, RESULTS
        ATOMS = {}
        PARAMS = {}
        RESULTS = {}

        #Castep_Python.finalise()

    @staticmethod
    @requires_env(CastepEnv)
    def update_params(mpi_comm, new_params):
        """Update the parameters set"""
        from castep_python import Castep_Python
        # Do some validation checking here
        pass

        # Now update the saved params
        PARAMS.update(new_params)

        # Now pass these new params to the code
        for key, value in new_params.items():
            Castep_Python.update_param(key, value)

    @staticmethod
    @requires_env(CastepEnv)
    def update_atoms(mpi_comm, new_atoms):
        """Update the atoms list"""
        from castep_python import Castep_Python
        global ATOMS

        # Optional validation checking
        if (new_atoms.get_atomic_numbers() != ATOMS.get_atomic_numbers()).any():
            raise NotImplementedError("Castep does not support changing atomic species")

        # Attach units to pos and lattice
        pos = new_atoms.get_positions().T * units.angstrom 
        lattice = new_atoms.get_cell() * units.angstrom   

        # # Update lattice if that changed

        if (new_atoms.get_cell() != ATOMS.get_cell()).any():
            Castep_Python.update_lattice_and_positions(lattice.to(units.bohr).magnitude, pos.to(units.bohr).magnitude)
        else:
            # Otherwise just update the positions
            Castep_Python.update_positions(pos.to(units.bohr).magnitude)

        # Save current atoms
        ATOMS = new_atoms


    @staticmethod
    @requires_env(CastepEnv)
    def update_atoms_extrap(mpi_comm, new_atoms):
        """Update the atoms list"""
        from castep_python import Castep_Python
        global ATOMS

        # Optional validation checking
        if (new_atoms.get_atomic_numbers() != ATOMS.get_atomic_numbers()).any():
            raise NotImplementedError("Castep does not support changing atomic species")

        pos = new_atoms.get_positions().T * units.angstrom

        # Now update saved atoms
        Castep_Python.update_positions_extrap(pos.to(units.bohr).magnitude)
        ATOMS = new_atoms

        
    @staticmethod
    @requires_env(CastepEnv)
    def calculate(mpi_comm, want_forces=False, want_stress=False):
        """Do the actual calculation"""
        from castep_python import Castep_Python
        global RESULTS

        num_atoms = len(ATOMS.get_atomic_numbers())

        # Call re-entrant castep method
        energy = Castep_Python.calculate_energy()

        # Set results
        RESULTS = Results(energy * units.hartree)
        RESULTS.free_energy = RESULTS.energy

        if want_forces:
            forces = np.empty((3, num_atoms), order='F')
            Castep_Python.calculate_forces(forces)
            RESULTS.forces = forces.T * units.hartree / units.bohr

        if want_stress:
            stress = np.empty(6, order='F')
            Castep_Python.calculate_stress(stress)
            RESULTS.stress = stress * units.hartree / units.bohr**3

        # Broadcast results to all nodes and return
        mpi_comm.bcast(RESULTS)
        return RESULTS

    @staticmethod
    @requires_env(CastepEnv)
    def get_results(mpi_comm):
        return RESULTS

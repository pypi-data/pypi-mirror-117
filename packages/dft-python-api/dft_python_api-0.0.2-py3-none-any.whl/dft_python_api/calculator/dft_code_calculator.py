#!/usr/bin/env python3
"""Main entry point for project"""
from ..tasks.task import Task
from ..master.master_io import Worker
from ..utils import units
import numpy as np
import functools
from inspect import getcallargs
from ase.calculators.calculator import Calculator, PropertyNotImplementedError, compare_atoms
from ase.units import Bohr, Hartree
from time import sleep

# Fancy print function call and args
def debug_print_entry(func):
    @functools.wraps(func)
    def wrapped(self, *args, **kwargs):
        if self.debug:
            output = f"Called {func.__name__}"
            fancy_kwargs = getcallargs(func, self, *args, **kwargs)
            arg_str = "(" + ",".join(f"{k}={v}" for k,v in fancy_kwargs.items() if k != "self") + ")"
            print(output + arg_str)
        return func(self, *args, **kwargs)
    return wrapped

# Conversion helper from pint to ase units. The exact units don't matter so 
# long as they correspond to the same thing in both libraries
ase_units = {
    'energy': (units.hartree, Hartree),
    'free_energy': (units.hartree, Hartree),
    'forces': (units.hartree/units.bohr, Hartree/Bohr),
    'stress': (units.hartree/units.bohr**3, Hartree/Bohr**3)
}

class DFT_Calculator(Calculator):
    implemented_properties = ['energy','forces','stress','free_energy']
    ignored_changes = {}
    discard_results_on_any_change = True

    def __init__(self, atoms=None, label='run', calculator_type=None, debug=False, num_mpi_processes=1,
                **kwargs):
        
        self.worker_started = False
        self.initialised = False
        self.reset_needed = False
        self.num_processes = num_mpi_processes
        self.worker = None
        self.debug = debug

        assert issubclass(calculator_type, Task), "Must pass a DFT calculator task type!"
        self.dft = calculator_type

        self.default_parameters = self.dft.get_default_parameters('energy', atoms)
        self.full_reset_flags = {'numbers'}

        super().__init__(atoms=atoms, label=label, **kwargs)
        
        self._start_dft()
        
    @debug_print_entry
    def _restart_dft(self):
        """Restart the DFT subprocess if required (ie if it has been initialised)"""
        if self.initialised:
            self._stop_dft()
            # print("resetting dft process")
        if not self.worker_started:
            self._start_dft()
        self.reset_needed = False


    def _start_dft(self):
        """Start the DFT code backend"""
        if self.worker_started:
            raise Exception("Tried to initialise an already initialised dft code!")

        # Start a worker manager and spawn a worker
        self.worker = Worker(self.label, self.num_processes)

        # Set flags to say this has been started but not initialised
        self.worker_started = True
        self.initialised = False

    def _stop_dft(self):
        """Stops the DFT code backend"""
        if not self.worker_started:
            raise Exception("Tried to end a worker that was already stopped!")

        # Send DFT finalisation task
        self.worker.add_task(0, self.dft(self.dft.finalise))
        self.worker.get_next_finished()
        self.worker.finish()

        # Give a small grace period and then kill it
        sleep(0.1)
        self.worker.kill()

        # Reset status flags
        self.worker = None
        self.worker_started = False
        self.initialised = False

    def set(self, **kwargs):
        # Since we can't change any parameters right now, we always restart
        changed_params = super().set(**kwargs)
        if changed_params:
            #  Mark for reset later on
            self.reset_needed = True

    @debug_print_entry
    def calculate(self, atoms=None, properties=None, system_changes=None):
        """Call the DFT code to calculate the requested properties"""

        # Check if we need to do a full reset
        if self.reset_needed or any(flag in system_changes for flag in self.full_reset_flags):
            self._restart_dft()

        # Make sure the worker is actually started
        if not self.worker_started:
            self._start_dft()

        # Make a copy of atoms
        if atoms is not None:
            self.atoms = atoms.copy()

        # Either initialise with these atoms or update these atoms
        if not self.initialised:
            self.worker.add_task(1, self.dft(self.dft.init, self.atoms, self.parameters))
            self.initialised = True
        elif system_changes:
            self.worker.add_task(1, self.dft(self.dft.update_atoms, self.atoms))

        # Do the ground state calculation
        want_forces = 'forces' in properties
        want_stress = 'stress' in properties
        self.worker.add_task(10, self.dft(self.dft.calculate, want_forces, want_stress))

        # ...and wait for the result
        task_id, result = self.worker.get_next_result()
        assert task_id == 10, "Wrong task number returned from DFT worker process"

        # Convert units to ASE and store in results
        for key,value in result.__dict__.items():
            if value is not None:
                try:
                    pint_unit, ase_unit = ase_units[key]
                except KeyError as exc:
                    raise Exception(f"{key} does not have a unit conversion") from exc
                
                self.results[key] = value.to(pint_unit).magnitude * ase_unit


    


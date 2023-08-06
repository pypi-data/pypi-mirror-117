"""Results class to hold results from calculations in a standard way"""
from . import units

default_energy_unit = units.hartree
default_force_unit = units.hartree / units.bohr

class Results:
    def __init__(self, energy=None, forces=None, stress=None, free_energy=None):
        self.energy = energy
        self.forces = forces
        self.stress = stress
        self.free_energy=free_energy


    def __repr__(self):
        return f"energy={self.energy}\tforces={self.forces}"

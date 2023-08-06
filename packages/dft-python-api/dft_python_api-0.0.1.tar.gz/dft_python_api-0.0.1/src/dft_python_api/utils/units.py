"""Defines a global set of units we can use to wrap outputs from DFT code"""
import pint

ureg = pint.UnitRegistry()
pint.set_application_registry(ureg)

hartree = ureg.sys.atomic.hartree
bohr = ureg.sys.atomic.bohr

eV = ureg.sys.SI.electron_volt
angstrom = ureg.sys.SI.angstrom

def mag(x, unit_value):
    return x.to(unit_value).magnitude
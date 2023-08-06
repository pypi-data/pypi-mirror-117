"""Module defining control flags that can be sent to the worker"""
from enum import Enum, auto, unique

@unique
class ControlFlag(Enum):
    """Defines some control flags that can be sent to/from the worker"""
    CONTINUE = auto()
    END = auto()
    CRASH = auto()
    WORKER_CRASHED = auto()

"""Module defining an environment (ie folder) that a task needs to run"""
# pylint: disable=too-few-public-methods
import glob
from pathlib import Path
import shutil
import os
from functools import wraps

def run_only_on_root(func):
    """Only runs func on the root node"""
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        if self.on_root:
            func(self, *args, **kwargs)
    return wrapped

class Envs:
    """Collection of all enviroments"""
    def __init__(self, worker_id, on_root):
        """Initialises a new set of environments"""
        self.envs = dict()
        self.worker_id = worker_id
        self.on_root = on_root
        self.root_dir = Path(".").resolve() # Save root folder from first call

    def get_env(self, env_type, mpi_comm):
        """
        Moves the CWD to the specified environment.
        Creates the environment if it doesn't already exist
        """
        if not env_type in self.envs:
            self.envs[env_type] = env_type(self.root_dir, self.worker_id, self.on_root).create()
            mpi_comm.barrier()
        self.envs[env_type].activate()

class Env:
    """Represents a working environment for a task"""
    def __init__(self, root_dir: Path, worker_id, on_root, working_dir = "work", **kwargs):
        """Sets up a environment for worker to work in"""
        # Store main paths in worker
        self.root = root_dir
        self.on_root = on_root
        self.worker_id = worker_id
        self.global_working_dir: Path = self.root / working_dir
        self.copy_list = []
        self.id_name = None

        # Run user provided initialisation with optional kwargs
        self.setup(**kwargs)
        self.local_working_dir = self.global_working_dir / f"worker-{worker_id}-{self.id_name}"

    def create(self):
        """Build actual local folder"""
        self._reset_folder()
        return self

    @run_only_on_root
    def _reset_folder(self):
        """Resets the environment to brand new"""
        self._make_working_dir(delete_old=False)
        if self.copy_list:
            self._do_copy()

    def setup(self):
        """
        Method that can be replaced by concrete workers.
        Should provide a unique name for the environment type.
        """
        raise NotImplementedError("Should override env setup to provide a name!")


    def activate(self):
        """Move cwd to working directory"""
        os.chdir(self.local_working_dir)

    @run_only_on_root
    def _make_working_dir(self, delete_old=True):
        """Creates the working directory for the task"""
        # Delete the old working dir if requested
        if delete_old and self.local_working_dir.exists():
            shutil.rmtree(self.local_working_dir)

        # Make the new folder ignoring whether it exists
        self.local_working_dir.mkdir(exist_ok=True, parents=True)

    @run_only_on_root
    def _do_copy(self):
        """Actually does the copy"""
        for file in self.copy_list:
            filename = file.name
            shutil.copy(file, self.local_working_dir / filename)

    @run_only_on_root
    def copy_files(self, copy_dir=None, copy_glob=None, copy_list=None):
        """Copies files from copy_dir to the working directory.
           You can specify the files to copy as either:
           copy_dir  - copy all the files in the folder
                       e.g. copy_file(copy_dir="myfiles")
           copy_glob - copy files matching a unix glob
                       e.g. copy_file(copy_glob="myfiles/proto.*")
           copy_list - copy all the files in the list
                       e.g. copy_file(copy_list=["myfiles/proto.param","myfiles/proto.cell"])
        """
        # Only root node does copying
        if not self.on_root:
            return

        if copy_dir:
            folder = self.root / copy_dir
            from_files = folder.iterdir()
        elif copy_glob:
            from_files = glob.glob(self.root / copy_glob)
        elif copy_list:
            from_files = map(lambda x: self.root/x, copy_list)
        else:
            raise ValueError("No items provided to copy")

        # Store these to be copied in a moment
        self.copy_list += list(from_files)

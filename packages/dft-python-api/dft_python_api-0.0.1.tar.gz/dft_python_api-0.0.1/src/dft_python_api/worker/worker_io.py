"""IO operations for worker.pyp"""
import sys
import pickle
import os

class ParentIO:
    """Class that handles receiving and communicating data to the parent python instance"""
    def __init__(self, comm):
        """Initialises a reader for io operations to the master process"""
        self.comm = comm
        self.rank = comm.Get_rank()
        self.isroot = self.rank == 0

        # Open named pipe
        if self.isroot:
            self.fname = self._recv()
            self.pipe = open(self.fname, 'wb')

    def _recv(self):
        """Read pickled object from stdin only on the root node"""
        if self.isroot:
            data = pickle.load(sys.stdin.buffer)
        else:
            data = None
        return data

    def recv_all(self):
        """Read pickled object from stdin and broadcast to all nodes"""
        return self.comm.bcast(self._recv())

    def send(self, data):
        """Send data to master process from root node"""
        if self.isroot:
            pickle.dump(data, self.pipe)
            self.pipe.flush()

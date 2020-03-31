from Logger.Policy.ILogPolicy import ILogPolicy
from Logger.Log import Log


class FilePolicy(ILogPolicy):

    def __init__(self, name):
        self._file = None
        self.open(name)

    def __del__(self):
        self.close()

    def open(self, name: str):
        if len(name) == 0:
            raise ValueError("ERROR: Must give valid filename (length > 0).")
        self.close()
        self._file = open(name, "w+")

    def write(self, log: Log):
        if self._file is None:
            raise ValueError("ERROR: File is not created or closed.")
        self._file.write(str(log) + "\n")

    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None

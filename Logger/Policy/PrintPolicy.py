from Logger.Log import Log
from Logger.Policy.ILogPolicy import ILogPolicy


class PrintPolicy(ILogPolicy):

    def __init__(self, name=""):
        pass

    def __del__(self):
        self.close()

    def open(self, name: str):
        pass

    def write(self, log: Log):
        print(Log)

    def close(self):
        pass

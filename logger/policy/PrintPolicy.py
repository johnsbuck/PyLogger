from logger.Log import Log
from logger.policy.ILogPolicy import ILogPolicy


class PrintPolicy(ILogPolicy):

    def __init__(self):
        pass

    def write(self, printlog: Log):
        print(printlog)

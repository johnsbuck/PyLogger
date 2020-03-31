from Logger.Log import Log
from Logger.Policy.ILogPolicy import ILogPolicy
from Logger.Policy.PrintPolicy import PrintPolicy
from Logger.SeverityType import SeverityType


class Logger(object):
    def __init__(self, policy=PrintPolicy()):
        if not issubclass(policy, ILogPolicy):
            raise ValueError("ERROR: Must use a proper log policy.")
        self._policy = policy
        self._lognum = 0

    def __del__(self):
        self.close()

    def open(self, name=""):
        self._policy.open(name=name)

    def close(self):
        self._policy.close()

    def log(self, severity: SeverityType, *args):
        msg = ""
        for arg in args:
            msg += str(arg)
        writelog = Log(self._lognum, severity, msg)
        self._lognum += 1
        self._policy.write(writelog)

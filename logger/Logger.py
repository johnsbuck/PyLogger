from logger.Log import Log
from logger.policy.ILogPolicy import ILogPolicy
from logger.policy.PrintPolicy import PrintPolicy
from logger.SeverityType import SeverityType


class Logger(object):
    def __init__(self, policy=PrintPolicy()):
        if not issubclass(type(policy), ILogPolicy):
            raise ValueError("ERROR: Must use a proper log policy.")
        self._policy = policy
        self._lognum = 0

    def log(self, severity: SeverityType, *args):
        msg = ""
        for arg in args:
            msg += str(arg)
        writelog = Log(self._lognum, severity, msg)
        self._lognum += 1
        self._policy.write(writelog)

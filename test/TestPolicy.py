from logger import Log
from logger.policy import ILogPolicy


class TestPolicy(ILogPolicy):

    def __init__(self):
        self.log_list = []
        self.openCount = 0

    def open(self, name=""):
        self.openCount += 1

    def write(self, log: Log):
        self.log_list.append(log)

    def close(self):
        self.openCount -= 1

import json
from datetime import datetime

from Logger.SeverityType import SeverityType


class Log(object):
    def __init__(self, lognum: int, severity=SeverityType.DEBUG, msg=""):
        self.lognum = lognum
        self.time = datetime.now().strftime("%Y-%b-%d %H:%M:%S.%f")
        self.time = self.time[:-3]
        self.severity = severity
        self.msg = msg

    def to_json(self):
        return json.JSONEncoder().encode(self.__dict__)

    def __str__(self):
        output = str(self.lognum).zfill(7) + " <" + self.time + "> ~ "
        output += self.severity.name + ": " + self.msg
        return output

    def __repr__(self):
        return self.__str__()
from Logger import *
from Logger.Policy import FilePolicy


logger = Logger(FilePolicy())
logger.open("test.txt")
logger.log(SeverityType.DEBUG, "Test")
logger.log(SeverityType.ERROR, "Test2")
logger.close()

import unittest

from logger import Logger, SeverityType
from test import TestPolicy


class TestLoggerMethods(unittest.TestCase):

    def test_logger_init(self):
        print("TEST_LOGGER_INIT Unit Test")

        print("\tAssert Logger.__init__ functions.")
        try:
            logger = Logger(TestPolicy())
        except Exception:
            self.fail("Logger.__init__ raised <Exception> unexpectedly.")

    def test_logger_log(self):
        print("TEST_LOGGER_LOG Unit Test")

        severity = SeverityType.DEBUG
        msg = "This is a log statement."

        logger = Logger(TestPolicy())

        print("\tAssert number of logs given to policy is 0.")
        self.assertEqual(len(logger._policy.log_list), 0)

        print("\tAssert Logger.log functions.")
        try:
            logger.log(severity, msg)
        except Exception:
            self.fail("Logger.log raised <Exception> unexpectedly.")

        print("\tAssert number of logs given to policy is 1.")
        self.assertEqual(len(logger._policy.log_list), 1)
        test_log = logger._policy.log_list[-1]

        print("\tAssert latest log contains expected values.")
        self.assertEqual(test_log.lognum, 0)
        self.assertEqual(test_log.severity, SeverityType.DEBUG)
        self.assertEqual(test_log.msg, msg)

        logger.log(severity, msg)

        print("\tAssert number of logs given to policy is 2.")
        self.assertEqual(len(logger._policy.log_list), 2)

        test_log = logger._policy.log_list[-1]

        print("\tAssert log number in latest log has incremented.")
        self.assertEqual(test_log.lognum, 1)


if __name__ == "__main__":
    unittest.main()

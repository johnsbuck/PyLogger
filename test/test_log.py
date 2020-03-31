import unittest
import json

from logger import *


class TestLogMethods(unittest.TestCase):

    def test_log_init(self):
        print("TEST_LOG_INIT Unit Test")

        lognum = 0
        severity = SeverityType.DEBUG
        msg = "Test Message."

        print("\tAssert Log.__init__ functions.")
        try:
            log1 = Log(lognum, severity, msg)
        except Exception:
            self.fail("Log.__init__ raised <Exception> unexpectedly.")

        print("\tAssert that the created Log object has the expected values.")
        self.assertEqual(log1.lognum, lognum)
        self.assertEqual(log1.severity, severity)
        self.assertEqual(log1.msg, msg)

        # Assert that Log object isn't connected to init method arguments
        lognum = lognum + 1
        severity = SeverityType.ERROR
        msg = "Another Test Message."

        print("\tAssert that the created Log object's members are not the same as the Log.__init__ arguments used.")
        self.assertNotEqual(log1.lognum, lognum)
        self.assertNotEqual(log1.severity, severity)
        self.assertNotEqual(log1.msg, msg)

    def test_log_eq(self):
        print("TEST_LOG_EQ Unit Test")

        lognum = 0
        severity = SeverityType.DEBUG
        msg = "Test Message."

        # Assert that two Logs with the same values are equal
        log1 = Log(lognum, severity, msg)
        log2 = Log(lognum, severity, msg)
        log2.time = log1.time

        print("\tAssert that the two created Log objects are the same.")
        try:
            self.assertTrue(log1 == log2)
        except Exception:
            self.fail("Log.__eq__ raised <Exception> unexpectedly.")

        try:
            self.assertFalse(log1 != log2)
        except Exception:
            self.fail("Log.__ne__ raised <Exception> unexpectedly.")

        # Assert that different Log numbers are not equal
        log2 = Log(lognum+1, severity, msg)
        log2.time = log1.time

        print("\tAssert that the Log objects not equal when the log numbers are different.")
        self.assertFalse(log1 == log2)
        self.assertTrue(log1 != log2)

        # Assert that different SeverityTypes are not equal
        log2 = Log(lognum, SeverityType.ERROR, msg)
        log2.time = log1.time

        print("\tAssert that the Log objects not equal when the SeverityTypes are different.")
        self.assertFalse(log1 == log2)
        self.assertTrue(log1 != log2)

        # Assert that different messages are not equal
        log2 = Log(lognum, severity, "Another " + msg)
        log2.time = log1.time

        print("\tAssert that the Log objects not equal when the messages are different.")
        self.assertFalse(log1 == log2)
        self.assertTrue(log1 != log2)

        # Assert that different times are not equal
        log2 = Log(lognum, severity, msg)
        log2.time = ""

        print("\tAssert that the Log objects not equal when the times are different.")
        self.assertFalse(log1 == log2)
        self.assertTrue(log1 != log2)

    def test_log_json(self):
        print("TEST_LOG_JSON Unit Test")
        lognum = 0
        severity = SeverityType.DEBUG
        msg = "Test Message."

        log = Log(lognum, severity, msg)

        print("\tAssert Log.to_json functions.")
        try:
            output = log.to_json()
        except Exception:
            self.fail("output.to_json raised <Exception> unexpectedly.")

        test_dict = json.JSONDecoder().decode(output)

        print("\tAssert JSON-decoded dictionary matches Log object dictionary.")
        self.assertEqual(test_dict, log.__dict__)


if __name__ == "__main__":
    unittest.main()

import sys
import unittest
import unitils

class TestUnitils(unittest.TestCase):
    def test_system_call_returns_out_err_rc(self):
        """A command which is shelled out using util.system_call
        should return stdout, stderr and the return code as a
        three-tuple
        """
        command = [sys.executable, "--version"]
        out, err, rc = unitils.util.system_call(command)
        self.assertIn("Python", out.decode("utf-8"))
        self.assertEqual(rc, 0)

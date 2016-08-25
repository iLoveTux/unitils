import os
import unittest
import unitils

try:
    from unittest import mock
except ImportError:
    import mock

dummy_path = os.pathsep.join([
    "/usr/bin",
    "/bin",
])
class TestWhich(unittest.TestCase):

    # Based on this mock, which should always return
    # the first path in os.environ["PATH"] joined with
    # the command to be searched for
    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.access", return_value=True)
    def test_finds_executable(self, mock_exists, mock_access):
        """Given a valid executable name which lies on the PATH,
        which should return the absolute path to that executable
        as a string.
        """
        os.environ["PATH"] = dummy_path
        results = unitils.which("ls")
        expected = "/usr/bin/ls"
        self.assertEqual(expected, results)

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.access", return_value=True)
    def test_finds_all_executables(self, mock_exists, mock_access):
        """When _all is True, which should return a generator which
        yields all the instances of cmd
        """
        os.environ["PATH"] = dummy_path
        results = list(unitils.which("ls", _all=True))
        expected = ["/usr/bin/ls", "/bin/ls"]
        self.assertEqual(expected, results)

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.access", return_value=False)
    def test_finds_all_executables(self, mock_exists, mock_access):
        """which should only match executable files
        """
        os.environ["PATH"] = dummy_path
        results = list(unitils.which("ls", _all=True))
        expected = []
        self.assertEqual(expected, results)


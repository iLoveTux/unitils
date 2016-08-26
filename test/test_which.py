import os
import unittest
import unitils
import platform

if "Windows" in platform.system():
    return_value_not_all = "C:\\Program Files\\ls"
    return_value_all = ["C:\\Program Files\\ls", "C:\\Program Files (x86)\\ls"]
    dummy_path = os.pathsep.join([
        "C:\\Program Files",
        "C:\\Program Files (x86)",
    ])
else:
    return_value_not_all = "/usr/bin/ls"
    return_value_all = ["/usr/bin/ls", "/bin/ls"]
    dummy_path = os.pathsep.join([
        "/usr/bin",
        "/bin",
    ])

try:
    from unittest import mock
except ImportError:
    import mock


class TestLsCLI(unittest.TestCase):

    @mock.patch("unitils.which", return_value=return_value_not_all)
    def test_can_be_called_with_just_cmd(self, mock_which):
        args = ["ls"]
        unitils.cli.which(argv=args)
        mock_which.assert_called_with(cmd="ls", _all=False)

    @mock.patch("unitils.which", return_value=return_value_all)
    def test_accepts_dash_a(self, mock_which):
        args = ["-a", "ls"]
        unitils.cli.which(argv=args)
        mock_which.assert_called_with(cmd="ls", _all=True)


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
        expected = return_value_not_all
        self.assertEqual(expected, results)

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.access", return_value=True)
    def test_finds_all_executables(self, mock_exists, mock_access):
        """When _all is True, which should return a generator which
        yields all the instances of cmd
        """
        os.environ["PATH"] = dummy_path
        results = list(unitils.which("ls", _all=True))
        expected = return_value_all
        self.assertEqual(expected, results)

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.access", return_value=False)
    def test_finds_only_executable_files(self, mock_exists, mock_access):
        """which should only match executable files
        """
        os.environ["PATH"] = dummy_path
        results = unitils.which("ls", _all=False)
        expected = None
        self.assertEqual(expected, results)

    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.access", return_value=False)
    def test_finds_all_executable_files(self, mock_exists, mock_access):
        """which should only match executable files
        """
        os.environ["PATH"] = dummy_path
        results = list(unitils.which("ls", _all=True))
        expected = []
        self.assertEqual(expected, results)


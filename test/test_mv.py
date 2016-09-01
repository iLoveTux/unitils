import unitils
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

class TestMvCli(unittest.TestCase):
    """General tests for the functionality of the mv.py cli
    """
    @mock.patch("unitils.mv")
    def test_accepts_src_and_dst(self, mock_mv):
        argv = ["/tmp/sample", "/tmp/.sample"]
        unitils.cli.mv(argv)
        mock_mv.assert_called_with(src="/tmp/sample",
                                   dst="/tmp/.sample")

class TestMv(unittest.TestCase):
    """General tests for the functionality of the mv callable
    """
    @mock.patch("shutil.move")
    def test_calls_shutil_move_with_args(self, mock_move):
        """Currently, unitils.mv is simply a wrapper around
        shutil.move. This works ok, will be waiting for feature
        requests to implement additional features.
        """
        unitils.mv("/tmp/sample", "/tmp/.sample")
        mock_move.assert_called_with(src="/tmp/sample",
                                     dst="/tmp/.sample")

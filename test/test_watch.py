import unittest
import unitils

try:
    from unittest import mock
except ImportError:
    import mock

def get_next(generator):
    try:
        return generator.next()
    except AttributeError:
        return next(generator)

return_value = (("out", "err", 0) for x in range(10))
class TestWatchCLI(unittest.TestCase):

    @mock.patch("unitils.watch", return_value=return_value)
    def test_watch_needs_command(self, mock_watch):
        args = []
        with self.assertRaises(SystemExit):
            unitils.cli.watch(args)

class TestWatch(unittest.TestCase):

    @mock.patch("unitils.system_call", return_value=("out", "err", 0))
    def test_watch_executes_command(self, mock_call):
        expected = ("out", "err", 0)
        result = unitils.watch(["test"])
        result = get_next(result)
        self.assertEqual(expected, result)

    @mock.patch("unitils.system_call", return_value=("out", "err", 0))
    @mock.patch("time.sleep")
    def test_watch_executes_command_every_two_seconds(self, mock_sleep, mock_call):
        from time import time
        expected = ("out", "err", 0)
        result = unitils.watch(["test"])
        get_next(result)
        t1 = time()
        get_next(result)
        t2 = time()
        mock_sleep.assert_called_with(2)

from itertools import chain
import unittest
import unitils
from io import StringIO

try:
    from unittest import mock
except ImportError:
    import mock

class TestHeadCli(unittest.TestCase):
    """tests for the head.py cli
    """
    @mock.patch("unitils.head")
    def test_will_take_one_argument_as_filename(self, mock_head):
        argv = ["/tmp/sample"]
        unitils.cli.head(argv)
        mock_head.assert_called_with(files=["/tmp/sample"],
                                     lines=10,
                                     verbose=False,
                                     quiet=False)

    @mock.patch("unitils.head")
    def test_will_take_more_than_one_argument_as_filenames(self, mock_head):
        argv = ["/tmp/sample"] * 2
        unitils.cli.head(argv)
        mock_head.assert_called_with(files=["/tmp/sample"] * 2,
                                     lines=10,
                                     verbose=False,
                                     quiet=False)

    @mock.patch("unitils.head")
    def test_will_take_dash_n_for_lines(self, mock_head):
        argv = ["-n", "5", "/tmp/sample"]
        unitils.cli.head(argv)
        mock_head.assert_called_with(files=["/tmp/sample"],
                                     lines=5,
                                     verbose=False,
                                     quiet=False)

    @mock.patch("unitils.head")
    def test_will_take_dash_q_for_quiet(self, mock_head):
        argv = ["-q", "/tmp/sample"]
        unitils.cli.head(argv)
        mock_head.assert_called_with(files=["/tmp/sample"],
                                     lines=10,
                                     verbose=False,
                                     quiet=True)

    @mock.patch("unitils.head")
    def test_will_take_dash_v_for_verbose(self, mock_head):
        argv = ["-v", "/tmp/sample"]
        unitils.cli.head(argv)
        mock_head.assert_called_with(files=["/tmp/sample"],
                                     lines=10,
                                     verbose=True,
                                     quiet=False)


test_file_1 = StringIO("\n".join(("line {}".format(n) for n in range(1, 21))))
test_file_1.name = "test.file.1"
test_file_2 = StringIO("\n".join(("line {}".format(n) for n in range(1, 21))))
test_file_2.name = "test.file.2"
class TestHead(unittest.TestCase):
    """General tests for the head callable
    """
    def setUp(self):
        test_file_1.seek(0)
        test_file_2.seek(0)

    def test_accept_file_like_object(self):
        expected = list("line {}\n".format(n) for n in range(1, 11))
        results = list(unitils.head(test_file_1))
        self.assertEqual(expected, results)

    def test_accepts_multiple_file_like_objects(self):
        expected_keys = ["test.file.1", "test.file.2"]
        expected_values = list([
            list("line {}\n".format(n) for n in range(1, 11)),
            list("line {}\n".format(n) for n in range(1, 11))
        ])
        expected = dict(zip(expected_keys, expected_values))
        results = unitils.head([test_file_1, test_file_2])
        for key in results.keys():
            results[key] = list(results[key])
        self.assertEqual(expected, results)

    @mock.patch("io.open", return_value=test_file_1)
    def test_accept_filename(self, mock_open):
        expected = list("line {}\n".format(n) for n in range(1, 11))
        results = list(unitils.head("/tmp/sample"))
        self.assertEqual(expected, results)

    @mock.patch("io.open", side_effect=[test_file_1, test_file_2])
    def test_accept_multiple_filenames(self, mock_open):
        expected_keys = ["test.file.1", "test.file.2"]
        expected_values = list([
            list("line {}\n".format(n) for n in range(1, 11)),
            list("line {}\n".format(n) for n in range(1, 11))
        ])
        expected = dict(zip(expected_keys, expected_values))
        results = unitils.head(["/tmp/sample", "/tmp/sample"])
        for key in results.keys():
            results[key] = list(results[key])
        self.assertEqual(expected, results)

    def test_accepts_argument_n(self):
        expected = list("line {}\n".format(n) for n in range(1, 5+1))
        results = list(unitils.head(test_file_1, lines=5))
        self.assertEqual(expected, results)

    def test_accepts_argument_verbose(self):
        expected = {
            "test.file.1": list("line {}\n".format(n) for n in range(1, 11))
        }
        results = unitils.head(test_file_1, verbose=True)
        results["test.file.1"] = list(results["test.file.1"])
        self.assertEqual(expected, results)

    def test_accepts_argument_quiet(self):
        expected = list(chain(
            ("line {}\n".format(n) for n in range(1, 11)),
            ("line {}\n".format(n) for n in range(1, 11))))
        results = list(unitils.head([test_file_1, test_file_2], quiet=True))
        self.assertEqual(expected, results)

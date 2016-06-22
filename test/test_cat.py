import sys
import unittest
import unitils
from unitils import cli
try:
    from unittest import mock
except ImportError:
    import mock

class TestCatCLI(unittest.TestCase):

    @mock.patch("unitils.cat", return_value=("this", "that", "the other"))
    def test_cat_defaults_to_stdin(self, mock_cat):
        args = []
        cli.cat(args)
        mock_cat.assert_called_with(files=[sys.stdin], number=False)

    @mock.patch("unitils.cat", return_value=("this", "that", "the other"))
    def test_cat_accepts_arbitrary_number_of_files(self, mock_cat):
        args = ["test-1.txt", "test-2.txt"]
        with self.assertRaises(SystemExit):
            cli.cat(args)

    @mock.patch("unitils.cat", return_value=((1, "this"), (2, "that"), (3, "the other")))
    def test_cat_accepts_accepts_number(self, mock_cat):
        args = ["-n"]
        cli.cat(args)
        mock_cat.assert_called_with(files=[sys.stdin], number=True)

data = (
    ("This", "That", "The other"),
    ("This", "That", "The other"),
)
class TestCat(unittest.TestCase):
    """General tests for cat's Python API
    """

    def test_cat_concatenates_nested_iterators(self):
        """given a list of lists of strings, cat should
        yield everything concatenated
        """
        expected = ["This", "That", "The other", "This", "That", "The other"]
        results  = list(unitils.cat(data))
        self.assertEqual(expected, results)

    def test_cat_supports_line_numbers(self):
        """given a list of lists of strings, cat should
        yield everything concatenated
        """
        expected = [
            (1, "This"),
            (2, "That"),
            (3, "The other"),
            (4, "This"),
            (5, "That"),
            (6, "The other")
        ]
        results  = list(unitils.cat(data, number=True))
        self.assertEqual(expected, results)

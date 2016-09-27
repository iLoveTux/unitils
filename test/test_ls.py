import unittest
import unitils
from io import StringIO

try:
    from unittest import mock
except ImportError:
    import mock

return_value = (
    'that',       'that',       'that',
    'the other',  'the other',  'the other',
    'this',       'this',       'this'
)
column_test_return_value = (
    "appveyor.yml",
    "cover",
    "docs",
    "Makefile",
    "requirements.txt",
    "setup.py",
    "test",
    "unitils",
    "codecov.yml",
    "dist",
    "LICENSE",
    "README.rst",
    "setup.cfg",
    "stats.dat",
    "test-data",
    "unitils.egg-info",
)
class TestLsCLI(unittest.TestCase):

    @mock.patch("unitils.ls", return_value=return_value)
    def test_can_be_called_without_arguments(self, mock_ls):
        args = []
        unitils.cli.ls(args)
        mock_ls.assert_called_with(path=".", _all=False, almost_all=False)

    @mock.patch("unitils.ls", return_value=column_test_return_value)
    @mock.patch("unitils.cli.get_terminal_size", return_value=(104, 25))
    def test_columns(self, mock_term_size, mock_ls):
        args = []
        out = StringIO()
        unitils.cli.ls(args, out=out)
        out.seek(0)
        results = out.read()
        expected = """appveyor.yml  cover  docs     Makefile    requirements.txt  setup.py   test       unitils           
codecov.yml   dist   LICENSE  README.rst  setup.cfg         stats.dat  test-data  unitils.egg-info  
"""
        self.assertEqual(expected, results)        


directory_listing = ["this", "that", "the other"] * 3
class TestLS(unittest.TestCase):

    @mock.patch("os.listdir", return_value=directory_listing)
    def test_ls_sorts_and_iterates_through_directory_listing(self, mock_listdir):
        """ls should be an iterator yielding the contents of the directory
        """
        expected = [
            'that',
            'that',
            'that',
            'the other',
            'the other',
            'the other',
            'this',
            'this',
            'this'
        ]
        results = list(unitils.ls())
        self.assertEqual(expected, results)

    @mock.patch("os.listdir", return_value=directory_listing+[".hidden"])
    def test_ls_ignores_dot_files(self, mock_listdir):
        """By default, ls should not yield any items staring with "."
        """
        expected = [
            'that',
            'that',
            'that',
            'the other',
            'the other',
            'the other',
            'this',
            'this',
            'this'
        ]
        results = list(unitils.ls())
        self.assertEqual(expected, results)

    @mock.patch("os.listdir", return_value=directory_listing+[".hidden"])
    def test_ls_accepts_all(self, mock_listdir):
        """If _all=True, ls should yield the "dot files" as well
        as "." and "..". Note that the param is "_all" that is because
        all is reserved in Python
        """
        expected = [
            '.',
            '..',
            '.hidden',
            'that',
            'that',
            'that',
            'the other',
            'the other',
            'the other',
            'this',
            'this',
            'this'
        ]
        results = list(unitils.ls(_all=True))
        self.assertEqual(expected, results)

    @mock.patch("os.listdir", return_value=directory_listing+[".hidden"])
    def test_ls_accepts_almost_all(self, mock_listdir):
        """If almost_all=True, ls should yield the "dot files" but not
        "." and "..".
        """
        expected = [
            '.hidden',
            'that',
            'that',
            'that',
            'the other',
            'the other',
            'the other',
            'this',
            'this',
            'this'
        ]
        results = list(unitils.ls(almost_all=True))
        self.assertEqual(expected, results)

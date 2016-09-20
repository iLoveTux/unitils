import os
import re
import sys
import unitils
import unittest
import colorama
from time import sleep
from unitils import cli
from io import StringIO
try:
    from unittest import mock
except ImportError:
    import mock


def magenta(text):
    return "{}{}{}".format(
        colorama.Fore.MAGENTA,
        text,
        colorama.Fore.RESET
    )

def green(text):
    return "{}{}{}".format(
        colorama.Fore.GREEN,
        text,
        colorama.Fore.RESET
    )

def red(text):
    return "{}{}{}".format(
        colorama.Fore.RED,
        text,
        colorama.Fore.RESET
    )

return_value = (
    "this\n",
    "that\n",
    "the other\n"
)
class TestGrepCLI(unittest.TestCase):

    @mock.patch("unitils.grep", return_value=return_value)
    def test_expr_needs_to_be_there(self, mock_grep):
        args = []
        with self.assertRaises(SystemExit):
            unitils.cli.grep(args)

    @mock.patch("unitils.grep", return_value=return_value)
    def test_files_defaults_to_stdin(self, mock_grep):
        args = ["*"]
        unitils.cli.grep(args)
        mock_grep.assert_called_with(
            expr="*",
            files=[sys.stdin],
            line_numbers=False,
            filenames=False,
            color=True,
            invert_match=False,
            ignore_case=False
        )

    @mock.patch("unitils.grep", return_value=return_value)
    def test_does_not_strip_trailing_whitespace(self, mock_grep):
        args = ["that"]
        out = StringIO()
        unitils.cli.grep(args, out=out)
        out.seek(0)
        self.assertEqual(out.read(), "this\nthat\nthe other\n")

test_data = (
    u"line 1",
    u"1 line",
    u"Line 1",
    u"1 Line",
    u"this",
    u"that",
    u"the other"
)
class TestGrep(unittest.TestCase):

    def test_grep_will_find_lines(self):
        """given regex, grep should find all occurances within file
        """
        expected = [
            "1 line",
            "1 Line",
        ]
        results = list(unitils.grep(r"^\d+.*", test_data))
        self.assertEqual(results, expected)

    def test_grep_will_find_lines_with_compiled_regex(self):
        """given regex as compiled regular expression, grep should find
        all occurances within file
        """
        expected = [
            "1 line",
            "1 Line",
        ]
        results = list(unitils.grep(re.compile(r"^\d+.*"), test_data))
        self.assertEqual(results, expected)

    def test_line_numbers(self):
        """if line_numbers is True, grep should prepend line numbers
        """
        expected = [
            "2: 1 line",
            "4: 1 Line",
        ]
        results = list(unitils.grep(r"^\d+.*", test_data, line_numbers=True))
        self.assertEqual(results, expected)

    def test_with_filename(self):
        """if line_numbers is True, grep should prepend line numbers
        """
        expected = [
            "<stdin>: 2: 1 line",
            "<stdin>: 4: 1 Line",
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            test_data,
            line_numbers=True,
            filenames=True
        ))
        self.assertEqual(results, expected)

    def test_with_list_of_filenames(self):
        """given regex, grep should find all occurances within file
        """
        expected = [
            "1 line",
            "1 Line",
            "1 line",
            "1 Line",
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            [test_data, test_data]
        ))
        self.assertEqual(results, expected)

    def test_with_file_object(self):
        """given regex, grep should find all occurances within file object
        """
        expected = [
            "1 line\n",
            "1 Line\n",
        ]
        fp = StringIO("\n".join(test_data))
        results = list(unitils.grep(r"^\d+.*", fp))
        self.assertEqual(results, expected)

    def test_color_will_be_added_when_color_is_true(self):
        expected = [
            "{}: {}: {}".format(
                magenta("<stdin>"),
                green("2"),
                red("1 line")
            ),
            "{}: {}: {}".format(
                magenta("<stdin>"),
                green("4"),
                red("1 Line")
            ),
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            test_data,
            line_numbers=True,
            filenames=True,
            color=True
        ))
        self.assertEqual(results, expected)

    def test_invert_selection(self):
        expected = [
        "<stdin>: 1: line 1",
        "<stdin>: 3: Line 1",
        "<stdin>: 5: this",
        "<stdin>: 6: that",
        "<stdin>: 7: the other",
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            test_data,
            line_numbers=True,
            filenames=True,
            invert_match=True
        ))
        self.assertEqual(results, expected)

    def test_color_match_works_as_expected(self):
        expected = re.sub(
            r"\w",
            red(r"\g<0>"),
            """    for line in grep(r"\d+:\s\w+", "/path/to/file"):\n""",
        )
        expected = "{}: {}".format(magenta("test.dat"), expected)
        content = u"""In addition to the command line utilities, you will also have a Python library which
contains the same functionality. I have routinely found it useful to be able to
use functions like this in Python source::

    from unitils import grep

    for line in grep(r"\d+:\s\w+", "/path/to/file"):
        num, word = line.split(":")

Of course that is a contrived example, but you get the idea.
"""
        fp = StringIO(content)
        fp.name = "test.dat"
        results = list(unitils.grep(
            r"\w",
            fp,
            color=True,
            filenames=True
        ))
        self.assertIn(expected, results)

    def test_case_insensitive_search(self):
        expected = [
            "line 1",
            "Line 1"
        ]
        results = list(unitils.grep(r"line 1", test_data, ignore_case=True))
        self.assertEqual(sorted(expected), sorted(results))

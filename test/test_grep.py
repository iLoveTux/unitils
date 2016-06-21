import os
import re
from io import StringIO
from time import sleep
import unitils
import unittest
import colorama

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
        content = u"""In addition to the command line utilities, you will also have a Python library which
contains the same functionality. I have routinely found it useful to be able to
use functions like this in Python source::

    from unitils import grep

    for line in grep(r"\d+:\s\w+", "/path/to/file"):
        num, word = line.split(":")

Of course that is a contrived example, but you get the idea.
"""
        fp = StringIO(content)
        results = list(unitils.grep(
            r"\w",
            fp,
            color=True
        ))
        self.assertIn(expected, results)

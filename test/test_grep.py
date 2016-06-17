import os
import re
from time import sleep
import unitils
import unittest
import colorama
from tempfile import NamedTemporaryFile as temp_file
from .util import make_file_for_grep_tests

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

test_data = """line 1
1 line
Line 1
1 Line
this
that
the other
"""

class TestGrep(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_file_1 = make_file_for_grep_tests()
        cls.test_file_2 = make_file_for_grep_tests()

    @classmethod
    def tearDownClass(cls):
        pass
#        os.remove(cls.test_file_1)
#        os.remove(cls.test_file_2)

    def test_grep_will_find_lines(self):
        """given regex, grep should find all occurances within file
        """
        expected = [
            "1 line\n",
            "1 Line\n",
        ]
        results = list(unitils.grep(r"^\d+.*", self.test_file_1))
        self.assertEqual(results, expected)

    def test_line_numbers(self):
        """if line_numbers is True, grep should prepend line numbers
        """
        expected = [
            "2: 1 line\n",
            "4: 1 Line\n",
        ]
        results = list(unitils.grep(r"^\d+.*", self.test_file_1, line_numbers=True))
        self.assertEqual(results, expected)

    def test_with_filename(self):
        """if line_numbers is True, grep should prepend line numbers
        """
        expected = [
            "{}: 2: 1 line\n".format(self.test_file_1),
            "{}: 4: 1 Line\n".format(self.test_file_1),
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            self.test_file_1,
            line_numbers=True,
            filenames=True
        ))
        self.assertEqual(results, expected)

    def test_with_list_of_filenames(self):
        """given regex, grep should find all occurances within file
        """
        expected = [
            "1 line\n",
            "1 Line\n",
            "1 line\n",
            "1 Line\n",
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            [self.test_file_1, self.test_file_2]
        ))
        self.assertEqual(results, expected)

    def test_with_file_object(self):
        """given regex, grep should find all occurances within file object
        """
        expected = [
            "1 line\n",
            "1 Line\n",
        ]
        with open(self.test_file_1, "r") as fp:
            results = list(unitils.grep(r"^\d+.*", fp))
        self.assertEqual(results, expected)

    def test_color_will_be_added_when_color_is_true(self):
        expected = [
            "{}: {}: {}\n".format(
                magenta(self.test_file_1),
                green("2"),
                red("1 line")
            ),
            "{}: {}: {}\n".format(
                magenta(self.test_file_1),
                green("4"),
                red("1 Line")
            ),
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            self.test_file_1,
            line_numbers=True,
            filenames=True,
            color=True
        ))
        self.assertEqual(results, expected)

    def test_invert_selection(self):
        expected = [
        "{}: 1: line 1\n".format(self.test_file_1),
        "{}: 3: Line 1\n".format(self.test_file_1),
        "{}: 5: this\n".format(self.test_file_1),
        "{}: 6: that\n".format(self.test_file_1),
        "{}: 7: the other\n".format(self.test_file_1),
        ]
        results = list(unitils.grep(
            r"^\d+.*",
            self.test_file_1,
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
        content = b"""In addition to the command line utilities, you will also have a Python library which
contains the same functionality. I have routinely found it useful to be able to
use functions like this in Python source::

    from unitils import grep

    for line in grep(r"\d+:\s\w+", "/path/to/file"):
        num, word = line.split(":")

Of course that is a contrived example, but you get the idea.
"""
        filename = make_file_for_grep_tests(test_data=content)
        results = list(unitils.grep(
            r"\w",
            filename,
            color=True
        ))
        self.assertIn(expected, results)
        os.remove(filename)

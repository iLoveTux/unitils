import re
import unitils
import unittest
import colorama
from tempfile import NamedTemporaryFile as temp_file

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

    def test_grep_will_find_lines(self):
        """given regex, grep should find all occurances within file
        """
        expected = [
            "1 line\n",
            "1 Line\n",
        ]
        with temp_file(dir=".") as tmp:
            tmp.write(test_data.encode("utf-8"))
            tmp.flush()
            filename = tmp.name
            results = list(unitils.grep(r"^\d+.*", filename))
        self.assertEqual(results, expected)

    def test_line_numbers(self):
        """if line_numbers is True, grep should prepend line numbers
        """
        expected = [
            "2: 1 line\n",
            "4: 1 Line\n",
        ]
        with temp_file(dir=".") as tmp:
            tmp.write(test_data.encode("utf-8"))
            tmp.flush()
            filename = tmp.name
            results = list(unitils.grep(r"^\d+.*", filename, line_numbers=True))
        self.assertEqual(results, expected)

    def test_with_filename(self):
        """if line_numbers is True, grep should prepend line numbers
        """
        with temp_file(dir=".") as tmp:
            filename = tmp.name
            expected = [
                "{}: 2: 1 line\n".format(filename),
                "{}: 4: 1 Line\n".format(filename),
            ]
            tmp.write(test_data.encode("utf-8"))
            tmp.flush()
            results = list(unitils.grep(
                r"^\d+.*",
                filename,
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
        with temp_file(dir=".") as tmp_1, temp_file(dir=".") as tmp_2:
            tmp_1.write(test_data.encode("utf-8"))
            tmp_2.write(test_data.encode("utf-8"))
            tmp_1.flush()
            tmp_2.flush()
            filename_1 = tmp_1.name
            filename_2 = tmp_2.name
            results = list(unitils.grep(r"^\d+.*", [filename_1, filename_2]))
        self.assertEqual(results, expected)

    def test_with_file_object(self):
        """given regex, grep should find all occurances within file object
        """
        expected = [
            "1 line\n",
            "1 Line\n",
        ]
        with temp_file("w+") as tmp:
            tmp.write(test_data)
            tmp.flush()
            tmp.seek(0)
            results = list(unitils.grep(r"^\d+.*", tmp.file))
        self.assertEqual(results, expected)

    def test_color_will_be_added_when_color_is_true(self):
        with temp_file(dir=".") as tmp:
            filename = tmp.name
            expected = [
                "{}: {}: {}\n".format(magenta(filename), green("2"), red("1 line")),
                "{}: {}: {}\n".format(magenta(filename), green("4"), red("1 Line")),
            ]
            tmp.write(test_data.encode("utf-8"))
            tmp.flush()
            results = list(unitils.grep(
                r"^\d+.*",
                filename,
                line_numbers=True,
                filenames=True,
                color=True
            ))
        self.assertEqual(results, expected)

    def test_invert_selection(self):
        with temp_file(dir=".") as tmp:
            filename = tmp.name
            expected = [
            "{}: 1: line 1\n".format(filename),
            "{}: 3: Line 1\n".format(filename),
            "{}: 5: this\n".format(filename),
            "{}: 6: that\n".format(filename),
            "{}: 7: the other\n".format(filename),
            ]
            tmp.write(test_data.encode("utf-8"))
            tmp.flush()
            results = list(unitils.grep(
                r"^\d+.*",
                filename,
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
        with temp_file(dir=".") as tmp:
            tmp.write(content)
            tmp.flush()
            filename = tmp.name
            results = list(unitils.grep(
                r"\w",
                filename,
                color=True
            ))
        self.assertIn(expected, results)

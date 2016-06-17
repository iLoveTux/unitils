from tempfile import NamedTemporaryFile
from .util import make_file_for_grep_tests
import os
import unittest
import unitils

contents = """This is a test
this is only a test
"""

def prep_fp(fp):
    fp.write(contents.encode("utf-8"))
    fp.flush()
    fp.seek(0)
    return fp


class TestWC(unittest.TestCase):
    """General tests for wc
    """

    @classmethod
    def setUpClass(cls):
        cls.test_file_1 = make_file_for_grep_tests(test_data=contents)
        cls.test_file_2 = make_file_for_grep_tests(test_data=contents)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_file_1)
        os.remove(cls.test_file_2)

    def test_wc_counts_number_of_lines_words_and_bytes(self):
        """wc should be able to count the lines, words and bytes of
        files
        """
        expected = [(2, 9, 35, self.test_file_1)]
        results = list(unitils.wc((self.test_file_1,)))
        self.assertEqual(expected, results)

    def test_wc_will_yield_only_linecount(self):
        """wc(files, lines=True) should behave like `wc -l`
        """
        expected = [(2, self.test_file_1)]
        results = list(unitils.wc((self.test_file_1,), lines=True))
        self.assertEqual(expected, results)

    def test_wc_will_yield_only_byte_count(self):
        """wc(files, byte_count=True) should behave like `wc -c`
        """
        expected = [(35, self.test_file_1)]
        results = list(unitils.wc((self.test_file_1,), byte_count=True))
        self.assertEqual(expected, results)

    def test_wc_will_yield_only_word_count(self):
        """wc(files, words=True) should behave like `wc -w`
        """
        expected = [(9, self.test_file_1)]
        results = list(unitils.wc((self.test_file_1,), words=True))
        self.assertEqual(expected, results)

    def test_wc_will_yield_only_char_count(self):
        """wc(files, chars=True) should behave like `wc -m`
        """
        expected = [(35, self.test_file_1)]
        results = list(unitils.wc((self.test_file_1,), chars=True))
        self.assertEqual(expected, results)

    def test_wc_will_yield_all_fields(self):
        """wc(files, chars=True, lines=True, words=True,
        byte_count=True) should behave like `wc -cmlw`
        """
        expected = [(2, 9, 35, 35, self.test_file_1)]
        results = list(unitils.wc(
            (self.test_file_1,),
            chars=True,
            lines=True,
            words=True,
            byte_count=True,

        ))
        self.assertEqual(expected, results)

    def test_wc_will_yield_only_max_line_length(self):
        """wc(files, max_line_length=True) should behave like `wc -L`
        """
        expected = [(19, self.test_file_1)]
        results = list(unitils.wc((self.test_file_1,), max_line_length=True))
        self.assertEqual(expected, results)

    def test_wc_adds_totals_if_more_than_one_file(self):
        """If more than one file is specified, a total line should be
        added to the end of the output
        """
        expected = [
            (2, 9, 35, self.test_file_1),
            (2, 9, 35, self.test_file_2),
            (4, 18, 70, "total")
        ]
        results = list(unitils.wc((self.test_file_1, self.test_file_2)))
        self.assertEqual(expected, results)

    def test_wc_adds_totals_if_more_than_one_file_and_works_with_all_options(self):
        """All options should work with multiple files
        """
        expected = [
            (2, 9, 35, 35, 19, self.test_file_1),
            (2, 9, 35, 35, 19, self.test_file_2),
            (4, 18, 70, 70, 19, "total")
        ]
        results = list(unitils.wc(
            (self.test_file_1, self.test_file_2),
            chars=True,
            lines=True,
            words=True,
            byte_count=True,
            max_line_length=True
        ))
        self.assertEqual(expected, results)

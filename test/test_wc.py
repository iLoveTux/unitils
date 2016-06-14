from tempfile import NamedTemporaryFile
import unittest
import unitils

contents = """This is a test
this is only a test
"""

class TestWC(unittest.TestCase):
    """General tests for wc
    """
    def test_wc_counts_number_of_lines_words_and_bytes(self):
        """wc should be able to count the lines, words and bytes of
        files
        """
        with NamedTemporaryFile() as fp:
            fp.write(contents.encode("utf-8"))
            fp.flush()
            fp.seek(0)
            expected = [(2, 9, 35, fp.name)]
            # Must accept either a filename or a file-like object
            results = list(unitils.wc((fp,)))
            self.assertEqual(expected, results)
            results = list(unitils.wc((fp.name,)))
            self.assertEqual(expected, results)

    def test_wc_will_yield_only_linecount(self):
        """wc(files, lines=True) should behave like `wc -l`
        """
        with NamedTemporaryFile() as fp:
            fp.write(contents.encode("utf-8"))
            fp.flush()
            fp.seek(0)
            expected = [(2, fp.name)]
            results = list(unitils.wc((fp.name,), lines=True))
            self.assertEqual(expected, results)

    def test_wc_will_yield_only_byte_count(self):
        """wc(files, byte_count=True) should behave like `wc -c`
        """
        with NamedTemporaryFile() as fp:
            fp.write(contents.encode("utf-8"))
            fp.flush()
            fp.seek(0)
            expected = [(35, fp.name)]
            results = list(unitils.wc((fp.name,), byte_count=True))
            self.assertEqual(expected, results)

    def test_wc_will_yield_only_word_count(self):
        """wc(files, words=True) should behave like `wc -w`
        """
        with NamedTemporaryFile() as fp:
            fp.write(contents.encode("utf-8"))
            fp.flush()
            fp.seek(0)
            expected = [(9, fp.name)]
            results = list(unitils.wc((fp.name,), words=True))
            self.assertEqual(expected, results)

    def test_wc_will_yield_only_char_count(self):
        """wc(files, chars=True) should behave like `wc -m`
        """
        with NamedTemporaryFile() as fp:
            fp.write(contents.encode("utf-8"))
            fp.flush()
            fp.seek(0)
            expected = [(35, fp.name)]
            results = list(unitils.wc((fp.name,), chars=True))
            self.assertEqual(expected, results)

    def test_wc_will_yield_all_fields(self):
        """wc(files, chars=True, lines=True, words=True,
        byte_count=True) should behave like `wc -cmlw`
        """
        with NamedTemporaryFile() as fp:
            fp.write(contents.encode("utf-8"))
            fp.flush()
            fp.seek(0)
            expected = [(2, 9, 35, 35, fp.name)]
            results = list(unitils.wc(
                (fp.name,),
                chars=True,
                lines=True,
                words=True,
                byte_count=True,

            ))
            self.assertEqual(expected, results)

    def test_wc_will_yield_only_mac_line_length(self):
        """wc(files, max_line_length=True) should behave like `wc -L`
        """
        with NamedTemporaryFile() as fp:
            fp.write(contents.encode("utf-8"))
            fp.flush()
            fp.seek(0)
            expected = [(19, fp.name)]
            results = list(unitils.wc((fp.name,), max_line_length=True))
            self.assertEqual(expected, results)

    def test_wc_adds_totals_if_more_than_one_file(self):
        """If more than one file is specified, a total line should be
        added to the end of the output
        """
        with NamedTemporaryFile() as fp_1, NamedTemporaryFile() as fp_2:
            for fp in (fp_1, fp_2):
                fp.write(contents.encode("utf-8"))
                fp.flush()
                fp.seek(0)
            expected = [
                (2, 9, 35, fp_1.name),
                (2, 9, 35, fp_2.name),
                (4, 18, 70, "total")
            ]
            results = list(unitils.wc((fp_1.name, fp_2.name)))
            self.assertEqual(expected, results)

    def test_wc_adds_totals_if_more_than_one_file(self):
        """All options should work with multiple files
        """
        with NamedTemporaryFile() as fp_1, NamedTemporaryFile() as fp_2:
            for fp in (fp_1, fp_2):
                fp.write(contents.encode("utf-8"))
                fp.flush()
                fp.seek(0)
            expected = [
                (2, 9, 35, 35, 19, fp_1.name),
                (2, 9, 35, 35, 19, fp_2.name),
                (4, 18, 70, 70, 19, "total")
            ]
            results = list(unitils.wc(
                (fp_1.name, fp_2.name),
                chars=True,
                lines=True,
                words=True,
                byte_count=True,
                max_line_length=True
            ))
            self.assertEqual(expected, results)

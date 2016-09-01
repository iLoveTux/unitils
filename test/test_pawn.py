import sys
import unitils
import unittest

if sys.version_info[0] < 3:
    from io import BytesIO as StringIO
else:
    from io import StringIO

try:
    from unittest import mock
except ImportError:
    import mock

class TestPawnCli(unittest.TestCase):
    """General tests for the pawn.py cli
    """
    @mock.patch("unitils.pawn")
    def test_takes_two_arguments_script_and_input_file(self, mock_pawn):
        argv = ["{print(FIELDS[0])}", "input.txt"]
        unitils.cli.pawn(argv)
        mock_pawn.assert_called_with(
            script="{print(FIELDS[0])}",
            files=["input.txt"])


test_data = StringIO("""
This is a test
This is only a test
this is a test of your local Pawn interpreter
""")

test_data_2 = StringIO("""
This is a test
This is only a test
this is a test of your local Pawn interpreter
""")

test_script = StringIO("{print(LINE)}")

class TestPawn(unittest.TestCase):
    """General tests for the functionality of pawn
    """
    def setUp(self):
        test_data.seek(0)
        test_data_2.seek(0)

    def tearDown(self):
        test_data.seek(0)
        test_data_2.seek(0)

    def test_default_pattern(self):
        """The default pattern should match on every line
        """
        mock_out = StringIO()
        sys.stdout = mock_out
        script = u"{print(LINE)}"
        expected = test_data.read()
        test_data.seek(0)
        unitils.pawn(script, test_data)
        mock_out.seek(0)
        results = mock_out.read()
        sys.stdout = sys.__stdout__
        self.assertEqual(expected, results)

    def test_patterns(self):
        mock_out = StringIO()
        sys.stdout = mock_out
        script = u"""
            only{
                print(LINE)
            }
            Pawn{
                print("Found Pawn")
            }
        """
        expected = "\n".join((
            "This is only a test",
            "Found Pawn\n"
        ))
        unitils.pawn(script, test_data)
        mock_out.seek(0)
        results = mock_out.read()
        self.assertEqual(expected, results)
        sys.stdout = sys.__stdout__

    def test_BEGIN(self):
        mock_out = StringIO()
        sys.stdout = mock_out
        script = u"""
            BEGIN{
                print("BEGIN")
            }
            only{
                print(LINE)
            }
        """
        expected = "\n".join((
            "BEGIN",
            "This is only a test\n",
        ))
        unitils.pawn(script, test_data)
        mock_out.seek(0)
        results = mock_out.read()
        self.assertEqual(expected, results)
        sys.stdout = sys.__stdout__

    def test_END(self):
        mock_out = StringIO()
        sys.stdout = mock_out
        script = u"""
            END{
                print("END")
            }
            only{
                print(LINE)
            }
        """
        expected = "\n".join((
            "This is only a test",
            "END\n",
        ))
        unitils.pawn(script, test_data)
        mock_out.seek(0)
        results = mock_out.read()
        self.assertEqual(expected, results)
        sys.stdout = sys.__stdout__

    @mock.patch("io.open", return_value=test_data)
    def test_accepts_filename(self, mock_open):
        mock_out = StringIO()
        sys.stdout = mock_out
        script = u"{print(LINE)}"
        expected = test_data.read()
        test_data.seek(0)
        unitils.pawn(script, "/tmp/sample")
        mock_out.seek(0)
        results = mock_out.read()
        self.assertEqual(expected, results)
        sys.stdout = sys.__stdout__

    @mock.patch("io.open", side_effect=[test_data, test_data_2])
    def test_accepts_multiple_input_files(self, mock_open):
        mock_out = StringIO()
        sys.stdout = mock_out
        script = u"{print(LINE)}"
        expected = test_data.read()
        expected = expected + expected
        test_data.seek(0)
        unitils.pawn(script, [test_data, test_data_2])
        mock_out.seek(0)
        results = mock_out.read()
        self.assertEqual(expected, results)
        sys.stdout = sys.__stdout__

    @mock.patch("io.open", side_effect=[test_data, test_data_2])
    def test_accepts_multiple_input_files_by_filename(self, mock_open):
        mock_out = StringIO()
        sys.stdout = mock_out
        script = u"{print(LINE)}"
        expected = test_data.read()
        expected = expected + expected
        test_data.seek(0)
        unitils.pawn(script, ["/tmp/sample", "/tmp/sample"])
        mock_out.seek(0)
        results = mock_out.read()
        self.assertEqual(expected, results)
        sys.stdout = sys.__stdout__

    @mock.patch("os.path.isfile", return_value=True)
    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("io.open", return_value=test_script)
    def test_accepts_a_script_file(self, mock_open, mock_exists, mock_isfile):
        mock_out = StringIO()
        sys.stdout = mock_out
        expected = test_data.read()
        test_data.seek(0)
        unitils.pawn("/tmp/script", test_data)
        mock_out.seek(0)
        results = mock_out.read()
        self.assertEqual(expected, results)
        sys.stdout = sys.__stdout__

import os
import unittest
import unitils
import platform

try:
    from unittest import mock
except ImportError:
    import mock


class TestCpCli(unittest.TestCase):
    """Test the functionality of the cp.py cli
    """
    @mock.patch("unitils.cp")
    def test_only_needs_src_and_dst(self, mock_cp):
        argv = ["/tmp/doesnt.exist", "/tmp/still.not"]
        unitils.cli.cp(argv=argv)
        mock_cp.assert_called_with(src="/tmp/doesnt.exist",
                                   dst="/tmp/still.not",
                                   recursive=False,
                                   no_clobber=False)

    @mock.patch("unitils.cp")
    def test_respects_recursive_flag(self, mock_cp):
        argv = ["--recursive", "/tmp/doesnt.exist", "/tmp/still.not"]
        unitils.cli.cp(argv=argv)
        mock_cp.assert_called_with(src="/tmp/doesnt.exist",
                                   dst="/tmp/still.not",
                                   recursive=True,
                                   no_clobber=False)

    @mock.patch("unitils.cp")
    def test_respects_noclobber_flag(self, mock_cp):
        argv = ["--no-clobber", "/tmp/doesnt.exist", "/tmp/still.not"]
        unitils.cli.cp(argv=argv)
        mock_cp.assert_called_with(src="/tmp/doesnt.exist",
                                   dst="/tmp/still.not",
                                   recursive=False,
                                   no_clobber=True)

    @mock.patch("unitils.cp")
    def test_respects_noclobber_and_recursive_flags(self, mock_cp):
        argv = ["--no-clobber",
                "--recursive",
                "/tmp/doesnt.exist",
                "/tmp/still.not"]
        unitils.cli.cp(argv=argv)
        mock_cp.assert_called_with(src="/tmp/doesnt.exist",
                                   dst="/tmp/still.not",
                                   recursive=True,
                                   no_clobber=True)


class TestCp(unittest.TestCase):
    """Test the functionality of the cp python callable
    """

    @mock.patch("shutil.copy", return_value=None)
    def test_shutil_copy_gets_called(self, mock_copy):
        src, dst = "/tmp/doesnt.exist", "/tmp/still.not"
        unitils.cp(src, dst)
        mock_copy.assert_called_with(src=src, dst=dst)

    @mock.patch("shutil.copy", return_value=None)
    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.path.isfile", return_value=True)
    def test_shutil_copy_doesnt_get_called_if_no_clobber(self,
                                                         mock_isfile,
                                                         mock_exists,
                                                         mock_copy):
        src, dst = "/tmp/doesnt.exist", "/tmp/still.not"
        unitils.cp(src, dst, no_clobber=True)
        self.assertFalse(mock_copy.called)

    @mock.patch("shutil.copy", return_value=None)
    @mock.patch("os.path.exists", return_value=False)
    @mock.patch("os.path.isfile", return_value=False)
    def test_no_clobber_shutil_copy_gets_called_if_doesnt_exist(self,
                                                                mock_isfile,
                                                                mock_exists,
                                                                mock_copy):
        src, dst = "/tmp/doesnt.exist", "/tmp/still.not"
        unitils.cp(src, dst, no_clobber=True)
        mock_copy.assert_called_with(src=src, dst=dst)

    @mock.patch("shutil.copytree", return_value=None)
    def test_shutil_copytree_gets_called_if_recursive_is_True(self, mock_copytree):
        src, dst = "/tmp/doesnt.exist/", "/tmp/still.not"
        unitils.cp(src, dst, recursive=True)
        mock_copytree.assert_called_with(src=src, dst=dst)

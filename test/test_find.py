from __future__ import print_function
from .util import make_test_data_directory
import os
import shutil
import unitils
import unittest


class TestFind(unittest.TestCase):
    """Generic tests for unitils.find
    """

    @classmethod
    def setUpClass(cls):
        cls.test_data_dir = os.path.abspath(make_test_data_directory())
        cls.old_dir = os.path.abspath(os.getcwd())
        os.chdir(cls.test_data_dir)

    @classmethod
    def tearDownClass(cls):
        os.chdir(cls.old_dir)
        shutil.rmtree(cls.test_data_dir)

    def test_no_params_finds_all_files(self):
        """calling find() with no params should act like issuing "$ find"
        from the terminal.
        """
        expected = [
            ".",
            os.path.join(".", "test.txt"),
            os.path.join(".", "Test.txt"),
            os.path.join(".", "branch-1"),
            os.path.join(".", "branch-1", "test.txt"),
            os.path.join(".", "branch-1", "Test.txt"),
            os.path.join(".", "branch-1", "level-2"),
            os.path.join(".", "branch-1", "level-2", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "Test.txt"),
            os.path.join(".", "branch-1", "level-2", "test"),
            os.path.join(".", "branch-1", "level-2", "test", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "test", "Test.txt"),
        ]
        results = list(unitils.find())
        self.assertEqual(set(expected), set(results))

    def test_name_param_limits_like_it_should(self):
        """find(name="test.txt") should behave like "$ find . -name test.txt"
        """
        expected = [
            os.path.join(".", "test.txt"),
            os.path.join(".", "branch-1", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "test", "test.txt"),
        ]
        results = list(unitils.find(name="test.txt"))
        self.assertEqual(set(expected), set(results))

    def test_name_param_limits_like_it_should_for_directories(self):
        """find(name="branch-1") should behave like "$ find . -name branch-1"
        """
        expected = [
            os.path.join(".", "branch-1"),
        ]
        results = list(unitils.find(name="branch-1"))
        self.assertEqual(set(expected), set(results))

    def test_path_param_limits_like_it_should(self):
        """find("branch-1", name="test.txt") should behave like "$ find branch-1 -name test.txt"
        """
        expected = [
            os.path.join("branch-1", "test.txt"),
            os.path.join("branch-1", "level-2", "test.txt"),
            os.path.join("branch-1", "level-2", "test", "test.txt"),
        ]
        results = list(unitils.find(path="branch-1", name="test.txt"))
        self.assertEqual(set(expected), set(results))

    def test_relative_path_param_limits_like_it_should(self):
        """find("./branch-1", name="test.txt") should behave like "$ find ./branch-1 -name test.txt"
        """
        expected = [
            os.path.join(".", "branch-1", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "test", "test.txt"),
        ]
        results = list(unitils.find(path=os.path.join(".", "branch-1"), name="test.txt"))
        self.assertEqual(set(expected), set(results))

    def test_iname_param_limits_like_it_should(self):
        """find("./branch-1", iname="test.txt") should behave like "$ find ./branch-1 -iname test.txt"
        """
        expected = [
            os.path.join(".", "branch-1", "test.txt"),
            os.path.join(".", "branch-1", "Test.txt"),
            os.path.join(".", "branch-1", "level-2", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "Test.txt"),
            os.path.join(".", "branch-1", "level-2", "test", "test.txt"),
            os.path.join(".", "branch-1", "level-2", "test", "Test.txt"),
        ]
        results = list(unitils.find(path=os.path.join(".", "branch-1"), iname="test.txt"))
        self.assertEqual(set(expected), set(results))

    def test_type_param_limits_as_it_should(self):
        """find(ftype="d", name="name*")
        """
        expected = [
            os.path.join(".", "branch-1", "level-2", "test"),
        ]
        results = list(unitils.find(".", ftype="d", name="test*"))
        self.assertEqual(set(expected), set(results))

    def test_type_param_D_not_implemented(self):
        with self.assertRaises(NotImplementedError) as exc:
            list(unitils.find(ftype="D"))

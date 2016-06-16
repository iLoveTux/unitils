from __future__ import print_function
import os
import shutil
import unitils
import unittest
import tempfile

def setup_temp_dir(root):
    if os.path.exists(root):
        shutil.rmtree(root)
    os.mkdir(root)
    os.makedirs(os.path.join(root, "branch-1", "level-2", "test"))
    filenames = [
        os.path.join(root, "test.txt"),
        os.path.join(root, "branch-1", "test.txt"),
        os.path.join(root, "branch-1", "level-2", "test.txt"),
        os.path.join(root, "branch-1", "level-2", "test", "test.txt"),
        os.path.join(root, "Test.txt"),
        os.path.join(root, "branch-1", "Test.txt"),
        os.path.join(root, "branch-1", "level-2", "Test.txt"),
        os.path.join(root, "branch-1", "level-2", "test", "Test.txt"),
    ]
    for filename in filenames:
        with open(filename, "w") as fp:
            fp.write("Hello, world from: {}\n".format(filename))

class TestFind(unittest.TestCase):
    """Generic tests for unitils.find
    """

    root = os.path.join(".", "_temp_unitils")
    @classmethod
    def setUpClass(cls):
        setup_temp_dir(cls.root)
        cls.old_dir = os.getcwd()
        os.chdir(cls.root)

    @classmethod
    def tearDownClass(cls):
#        tear_down_temp_dir(cls.root)
        os.chdir(cls.old_dir)
        shutil.rmtree(cls.root)

    def test_no_params_finds_all_files(self):
        """calling find() with no params should act like issuing "$ find"
        from the terminal.
        """
        expected = [
            ".",
            "./test.txt",
            "./Test.txt",
            "./branch-1",
            "./branch-1/test.txt",
            "./branch-1/Test.txt",
            "./branch-1/level-2",
            "./branch-1/level-2/test.txt",
            "./branch-1/level-2/Test.txt",
            "./branch-1/level-2/test",
            "./branch-1/level-2/test/test.txt",
            "./branch-1/level-2/test/Test.txt",
        ]
        results = list(unitils.find())
        self.assertEqual(sorted(expected), sorted(results))

    def test_name_param_limits_like_it_should(self):
        """find(name="test.txt") should behave like "$ find . -name test.txt"
        """
        expected = [
            "./test.txt",
            "./branch-1/test.txt",
            "./branch-1/level-2/test.txt",
            "./branch-1/level-2/test/test.txt",
        ]
        results = list(unitils.find(name="test.txt"))
        self.assertEqual(sorted(expected), sorted(results))

    def test_name_param_limits_like_it_should_for_directories(self):
        """find(name="branch-1") should behave like "$ find . -name branch-1"
        """
        expected = [
            "./branch-1",
        ]
        results = list(unitils.find(name="branch-1"))
        self.assertEqual(sorted(expected), sorted(results))

    def test_path_param_limits_like_it_should(self):
        """find("branch-1", name="test.txt") should behave like "$ find branch-1 -name test.txt"
        """
        expected = [
            "branch-1/test.txt",
            "branch-1/level-2/test.txt",
            "branch-1/level-2/test/test.txt",
        ]
        results = list(unitils.find(path="branch-1", name="test.txt"))
        self.assertEqual(sorted(expected), sorted(results))

    def test_relative_path_param_limits_like_it_should(self):
        """find("./branch-1", name="test.txt") should behave like "$ find ./branch-1 -name test.txt"
        """
        expected = [
            "./branch-1/test.txt",
            "./branch-1/level-2/test.txt",
            "./branch-1/level-2/test/test.txt",
        ]
        results = list(unitils.find(path="./branch-1", name="test.txt"))
        self.assertEqual(sorted(expected), sorted(results))

    def test_iname_param_limits_like_it_should(self):
        """find("./branch-1", iname="test.txt") should behave like "$ find ./branch-1 -iname test.txt"
        """
        expected = [
            "./branch-1/test.txt",
            "./branch-1/Test.txt",
            "./branch-1/level-2/test.txt",
            "./branch-1/level-2/Test.txt",
            "./branch-1/level-2/test/test.txt",
            "./branch-1/level-2/test/Test.txt",
        ]
        results = list(unitils.find(path="./branch-1", iname="test.txt"))
        self.assertEqual(sorted(expected), sorted(results))

    def test_type_param_limits_as_it_should(self):
        """find(ftype="d", name="name*")
        """
        expected = [
            "./branch-1/level-2/test",
        ]
        results = list(unitils.find(".", ftype="d", name="test*"))
        self.assertEqual(sorted(expected), sorted(results))

    def test_type_param_D_not_implemented(self):
        with self.assertRaises(NotImplementedError) as exc:
            list(unitils.find(ftype="D"))

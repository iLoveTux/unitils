import os
import shutil
from uuid import uuid4 as uuid
from time import time, sleep


def make_test_data_directory(root="."):
    tmp_dir = os.path.join(root, "test-data")
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)
    os.makedirs(os.path.join(tmp_dir, "branch-1", "level-2", "test"))
    filenames = [
        os.path.join(tmp_dir, "test.txt"),
        os.path.join(tmp_dir, "branch-1", "test.txt"),
        os.path.join(tmp_dir, "branch-1", "level-2", "test.txt"),
        os.path.join(tmp_dir, "branch-1", "level-2", "test", "test.txt"),
        os.path.join(tmp_dir, "Test.txt"),
        os.path.join(tmp_dir, "branch-1", "Test.txt"),
        os.path.join(tmp_dir, "branch-1", "level-2", "Test.txt"),
        os.path.join(tmp_dir, "branch-1", "level-2", "test", "Test.txt"),
    ]
    for filename in filenames:
        with open(filename, "w") as fp:
            fp.write("Hello, world from: {}\n".format(filename))
            fp.flush()
            os.fsync(fp.fileno())
    return tmp_dir

_test_data = """line 1
1 line
Line 1
1 Line
this
that
the other
"""

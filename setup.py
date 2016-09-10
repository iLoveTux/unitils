import sys
from setuptools import setup

tests_require = ["nose"]
if sys.version_info < (3,0):
    tests_require = ["nose", "mock"]

setup(
    name="unitils",
    version="0.1.0",
    author="iLoveTux",
    author_email="me@ilovetux.com",
    description="Cross platform utilities I have found to be incredibly useful",
    license="GPLv3",
    keywords="utility tools cli",
    url="http://github.com/ilovetux/unitils",
    packages=['unitils'],
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "cat.py=unitils.cli:cat",
            "cp.py=unitils.cli:cp",
            "find.py=unitils.cli:find",
            "grep.py=unitils.cli:grep",
            "head.py=unitils.cli:head",
            "ls.py=unitils.cli:ls",
            "mv.py=unitils.cli:mv",
            "watch.py=unitils.cli:watch",
            "wc.py=unitils.cli:wc",
            "which.py=unitils.cli:which",
        ]
    },
    test_suite="nose.collector",
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

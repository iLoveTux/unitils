from setuptools import setup

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
    install_requires=[
        "lxml", "colorama", "blessings"
    ],
    entry_points={
        "console_scripts": [
            "grep.py=unitils.cli:grep",
            "find.py=unitils.cli:find",
            "wc.py=unitils.cli:wc",
            "cat.py=unitils.cli:cat",
            "ls.py=unitils.cli:ls",
        ]
    },
    test_suite="nose.collector",
    tests_require=["nose", "mock"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3",
    ],
)

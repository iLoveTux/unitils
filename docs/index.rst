.. unitils documentation master file, created by
   sphinx-quickstart on Sun Jun  5 18:00:41 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to unitils's documentation!
===================================

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

What is it and why do I care?
=============================

Unitils (a contraction of Unix and utils) is a set of tools loosly inspired by
utilities usually present on a unix platform. I have taken inspriation from these
tools and modified, simplified and rewrote them in Python 3.5. When you install
this package from PyPI, `pip install unitils`, you will have a number of commands
added to your PATH (assuming Python is on your PATH), these utilities are
cross platform and incredibly useful.

In addition to the command line utilities, you will also have a Python library which
contains the same functionality. I have routinely found it useful to be able to
use functions like this in Python source::

    from unitils import grep

    for line in grep(r"\d+:\s\w+", "/path/to/file"):
        num, word = line.split(":")

Of course that is a contrived example, but you get the idea.

Why should I use it?
====================

Unitils is a collection of useful utilities which have been re-written to be simple
and to provide a CLI as well as a Python API. A few considerations which went into
the design should be highlighted to understand why this was written and why it would
be useful.

Unitils was written to be:

    - `Fast <stats.dat>`_, everything is an iterator (where possible) and strives to be as efficient in both memory and cpu time. The linked download is the output of Python's cProfile, there are `tools <https://jiffyclub.github.io/snakeviz/>`_ with which you can visualize this data.

    - `Tested <cover.html>`_, Unittests are at and will remain at 100% test coverage.

    - Cross Platform, Written in Python these utilities can run on Windows, Linux and Mac OSx.

    - Provides an API to use these utilities in Python, cross-platform and without "shelling out".

    - Open Source, This project is released under the `GPLv3 <https://www.gnu.org/licenses/gpl.txt>`_


.. toctree::
   :maxdepth: 2

CLI Tools
=========

.. automodule:: unitils.cli
   :members:

API
===

.. automodule:: unitils
   :members:

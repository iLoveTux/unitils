What is it and why do I care?
-----------------------------

Unitils has been incredibly useful for my co-workers and myself. They are simplified, altered forms of common and useful utilities you are likely to find on most Unix-like operating systems. They are written as command line utilities, but also present a single Python function which can be used from within Python without "shelling" the command out.

Because of the simplified nature of these utilities along with the alterations made whether we had a choice or not. We wished to differentiate ourselves from similar commands which were there first. Each of our utilities appends ".py" to the end of the command. For instance, our version of `grep` can be invoked with the `grep.py` command (`grep.py.exe` on Windows).

For instance, `grep.py` is designed to be used just like this::

  $ grep.py -i 'warn' /var/log/*.log

And from Python it can be used like this::

  import os
  from unitils import grep

  # remember though that shell expansion was done by the system's shell above
  log_files = (f for f in os.listdir("/var/log/") if ".log" in f)
  for match in grep("warn", log_files, ignore_case=True):
      print(match)

Why should I use it?
--------------------

Unitils is a collection of useful utilities which have been re-written to be simple
and to provide a CLI as well as a Python API. A few considerations which went into
the design should be highlighted to understand why this was written and why it would
be useful.

Unitils was written to be:

    - Fast <stats.dat>, everything is an iterator (where possible) and strives to be as efficient in both memory and cpu time.

    - Tested <cover.html>, Unittests are at and will remain at 100% test coverage.

    - Cross Platform, Written in Python these utilities can run on Windows, Linux and Mac OSx.

    - Provides an API to use these utilities in Python, cross-platform and without "shelling out".

    - Open Source, This project is released under the `GPLv3 <https://www.gnu.org/licenses/gpl.txt>`_


How does it work?
-----------------

Each command we target, we create a Python iterator which yields the output and send it to stdout. So we in effect have native, memory efficient access to many common utilities directly from within Python.

How do I get it?
----------------

To get the most supported version::

  $ pip install unitils

To get the latest, "bleeding edge" version::

  $ pip install https://github.com/ilovetux/unitils/archive/master.zip

For the nightlies::

  $ pip install https://github.com/ilovetux/unitils/archive/dev.zip

How do I run the tests?
-----------------------

You can clone the repository and use the following command::

  $ make test

or alternately::

  $ python setup.py nosetests


In general, the master branch is what is available on PyPI.

What is this compatible with?
-----------------------------

Unitils was written targeting Python 3.5.1, but may work on other versions as well, we plan to add support for earlier versions in the future. Besides the version of Python, unitils should work on all platforms on which Python runs.

What is the current list of utilities provided by unitils?
----------------------------------------------------------

* find
* grep
* wc

What is on the list to be done?
-------------------------------

* ls
* ll
* cat
* top
* wget
* zip / unzip
* curl
* ssh
* make
* watch

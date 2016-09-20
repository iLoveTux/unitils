************
Introduction
************

.. image:: https://travis-ci.org/iLoveTux/unitils.svg?branch=master
    :alt: Travis-CI Build Status (for Linux)
    :target: https://travis-ci.org/iLoveTux/unitils

.. image:: https://ci.appveyor.com/api/projects/status/i8jnjgjojbr0scov?svg=true
    :alt: AppVeyor Build Status (for windows)
    :target: https://ci.appveyor.com/project/iLoveTux/unitils

.. image:: https://codecov.io/gh/iLoveTux/unitils/branch/master/graph/badge.svg
    :alt: Test Coverage Status
    :target: https://codecov.io/gh/iLoveTux/unitils

.. image:: https://codeclimate.com/github/iLoveTux/unitils/badges/gpa.svg
   :alt: Code Climate
   :scale: 100%
   :target: https://codeclimate.com/github/iLoveTux/unitils

.. image:: https://readthedocs.org/projects/docs/badge/?version=latest
    :alt: Documentation Status
    :target: http://unitils.readthedocs.io/en/latest/index.html

-----------------------------
What is it and why do I care?
-----------------------------

Unitils has been incredibly useful for my co-workers and myself. They are simplified, altered forms of common and useful utilities you are likely to find on most Unix-like operating systems. They are written as command line utilities, but also present a single Python generator which can be used from within Python without "shelling" the command out.

Because of the simplified nature of these utilities along with the compromises we have made. We wished to differentiate ourselves from similar commands which were our inspiration. Each of our utilities appends ".py" to the end of the command. For instance, our version of `grep` can be invoked with the `grep.py` command.

For instance, `grep.py` is designed to be used just like this::

  $ grep.py -i 'warn' /var/log/*.log

And from Python it can be used like this::

  from glob import iglob
  from unitils import grep

  for match in grep("warn", iglob('/var/log/*.log'), ignore_case=True):
      print(match)

--------------------
Why should I use it?
--------------------

Unitils is a collection of useful utilities which have been re-written to be simple
and to provide a CLI as well as a Python API.

Unitils was written to be:

    - Fast, everything is an generator (where possible) and strives to be as efficient in both memory and cpu time.

    - Tested, Unittests are important and we strive for high test coverage.

    - Cross Platform, Written in Python these utilities can run on Windows, Linux and Mac OSx.

    - Provides an API to use these utilities in Python, cross-platform and without "shelling out".

    - Open Source, This project is released under the `GPLv3 <https://www.gnu.org/licenses/gpl.txt>`_

-----------------
How does it work?
-----------------

Each command we target, we create a Python generator which yields the output and send it to stdout. So we in effect have native, memory efficient access to many common utilities directly from within Python. We then wrap a command line interface around this generator tp provide our users with a convenient cross-platform utility.

----------------
How do I get it?
----------------

To get the most supported version::

  $ pip install unitils

To get the latest version::

  $ pip install https://github.com/ilovetux/unitils/archive/master.zip

For the nightlies::

  $ pip install https://github.com/ilovetux/unitils/archive/dev.zip

-----------------------
How do I run the tests?
-----------------------

You can clone the repository and use the following command::

  $ make test

or alternately::

  $ python setup.py nosetests


In general, the master branch is what is available on PyPI.

-----------------------------
What is this compatible with?
-----------------------------

Unitils is tested and confirmed to work with

* Python 3.5
* Python 3.4
* Python 3.3
* Python 2.7
* pypy

Unitils should work on all platforms on which Python runs.

----------------------------------------------------------
What is the current list of utilities provided by unitils?
----------------------------------------------------------

* cat
* cp
* find
* grep
* head
* ls
* mv
* watch
* wc
* which

-------------------------------
What is on the list to be done?
-------------------------------


See `this issue <https://github.com/iLoveTux/unitils/issues/5>`_ for the state of
our current prgress.

---------------
How can I help?
---------------

You can do all the github type things, submit an issue in our `issue tracker <https://github.com/ilovetux/unitils/issues>`_ or fork and submit a `pull request <https://github.com/ilovetux/unitils/pulls>`_. If none of that appeals to you, you can always send me an email personally at me@ilovetux.com

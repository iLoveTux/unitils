# unitils

A set of simplified unix utility clones, which present a CLI and a Python API (without shelling out).

## What is it and why do I care?

Unitils has been incredibly useful for my co-workers and myself. They are simplified, altered forms of common and useful utilities you are likely to find on most Unix-like operating systems. They are written as command line utilities, but also present a single Python function which can be used from within Python without "shelling" the command out.

Because of the simplified nature of these utilities along with the alterations made whether we had a choice or not. We wished to differentiate ourselves from similar commands which were there first. Each of our utilities appends ".py" to the end of the command. For instance, our version of `grep` can be invoked with the `grep.py` command (`grep.py.exe` on Windows).

For instance, `grep.py` is designed to be used just like this:

```bash
$ grep.py -i 'warn' /var/log/*.log
```

And from Python it can be used like this:

```python
import os
from unitils import grep

# remember though that shell expansion was done by the system's shell above
log_files = (f for f in os.listdir("/var/log/") if ".log" in f)
for match in grep("warn", log_files, ignore_case=True):
    print(match)
```

## How does it work?

Each command we target, we create a Python iterator which yields the output and send it to stdout. So we in effect have native, memory efficient access to many common utilities directly from within Python.

## How do I get it?

To get the most supported version:

```bash
$ pip install unitils
```

To get the latest, "bleeding edge" version:

```bash
$ pip install https://github.com/ilovetux/unitils/archive/master.zip
```

For the nightlies:

```bash
$ pip install https://github.com/ilovetux/unitils/archive/dev.zip
```

## How do I run the tests?

You can clone the repository and use the following command:

```bash
$ make test
```

or alternately:

```bash
$ python setup.py nosetests
```

In general, the master branch is what is available on PyPI.

## What is this compatible with?

Unitils was written targeting Python 3.5.1, but may work on other versions as well, we plan to add support for earlier versions as well. Besides the version of Python, unitils should work on all platforms on which Python runs.

## What is the current list of utilities provided by unitils?

* find
* grep
* wc

## What is on the list to be done?

* ls
* ll
* cat
* top
* wget
* zip / unzip
* curl
* ssh


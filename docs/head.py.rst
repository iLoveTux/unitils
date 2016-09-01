head.py(1)
**********

Name
====

   head.py - Output the first part of files

SYNOPSIS
========

.. code:: bash

   head.py [OPTIONS]... [FILE]...

DESCRIPTION
===========

    head.py will send the first 10 lines of each file to stdout. If more
    than one file is specified each will be preceded by a header containing
    the filename

    This is a simplified clone of the well-known head command. Not all options
    for the original will be available for this command.

OPTIONS
=======

Generic Program Information
---------------------------

.. code::

    --help
        Output a usage message and exits.
    -n, --lines
        The number of lines to print
    -q, --quiet
        Never print the header with the filename
    -v, --verbose
        Always print the header with the filename

EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to become feature-compatible with head
as released by the Free Software Foundation.

ENVIRONMENT VARIABLES
=====================

No environment variables affect the behavior of this software

EXIT STATUS
===========

We aim to take advantage of exit status, but currently do not. The exit status
will be 0 unless an error occurs in which case it will be non-zero.

COPYRIGHT
=========

Copyright 2016 Clifford Bressette IV (iLoveTux).

This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

BUGS
====

Bugs can be reported in our
`issue tracker <https://github.com/ilovetux/unitils/issues>`_. This is also the
correct place for feature requests.

SEE ALSO
========

None yet

NOTES
=====

None yet

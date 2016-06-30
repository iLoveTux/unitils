find.py(1)
**********

Name
====

   find.py - Search for files in a directory heirarchy

SYNOPSIS
========

.. code:: bash

   find.py [OPTIONS...] [PATH]

DESCRIPTION
===========

    find.py currently differs greatly from the GNU implementation of find.
    We do not currently evaluate expressions. We believe that we can cover
    most common use cases with options rather than with a Domain Specific
    Language (DSL), if this is found not to be the case, we will re-evaluate.

    We try as much as possible to make the usage feel like the usage of the
    GNU find utility.

OPTIONS
=======

.. code::

    -iname=INAME
        The case-insensitive name spec (glob pattern) to search for.
    -name=NAME
        The case-sensitive name spec (glob pattern) to search for.
    -type=TYPE
        The type of file to look for. TYPE can be any of the following:

        b   block (buffered) special
        c   character (unbuffered) special
        d   directory
        p   named pipe (FIFO)
        f   regular file
        l   symbolic link
        s   socket

EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to become feature-compatible with find
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

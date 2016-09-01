cp.py(1)
**********

Name
====

   cp.py - Copy a file or directory

SYNOPSIS
========

.. code:: bash

   cp.py [OPTIONS] SRC DST

DESCRIPTION
===========

    cp.py copies a source file or directory to a destination. If dst is a
    directory, then a file with the same name as the original will be placed
    within the directory. If src is a directory, you should specify --recursive
    as this will allow the directory to be copied in full.

    This is a simplified clone of the well-known cp command. Not all options
    for the original will be available for this command.

OPTIONS
=======

Generic Program Information
---------------------------

.. code::

    --help
        Output a usage message and exits.
    -R, --recursive
        Recursively copy the contents of src to dst
    -n, --no-clobber
        If specified, files will not be copied if they already exist at dst

EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to become feature-compatible with cp
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

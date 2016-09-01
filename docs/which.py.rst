which.py(1)
**********

Name
====

   which.py - Search PATH for cmd and return the first instance

SYNOPSIS
========

.. code:: bash

   which.py [OPTIONS] CMD

DESCRIPTION
===========

    Searches the PATH for cmd and prints the first occurance. This means
    that the path printed will be the command invoked when cmd is issued.

    This is currently extremely limited compared to the GNU ls command,
    but improvements are expected to be done soon. If you need a specific
    feature to be completed please don't hesitate to open an issue in
    our `issue tracker <https://github.com/ilovetux/unitils>`_.

OPTIONS
=======

.. code::

    -h, --help
        Prints a usage message and exits
    -a, --all
        Prints all matches, not just the first one

EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to become feature-compatible with which
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

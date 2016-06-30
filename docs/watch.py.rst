watch.py(1)
**********

Name
====

   watch.py - execute a program periodically, displaying the results

SYNOPSIS
========

.. code:: bash

   wc.py [OPTIONS...] COMMAND

DESCRIPTION
===========

    watch.py runs COMMAND repeatedly, displaying its output and errors. This
    allows you to watch the program output change over time. By default, the
    program is run every two seconds. By default, watch.py will run until
    interrupted.

    NOTE: This program differs significantly in execution from the GNU version
    of watch. This is because I have not been able to find a way to go
    fullscreen within a Windows command prompt. Instead, we clear the screen
    before displaying the new output (cls on Windows and clear on *nix). If
    you know of a way to achieve the desired results in a cross-platform way
    within Python, please open an issue in our
    `issue tracker <https://github.com/ilovetux/unitils/issues>`_ or better yet,
    open a `pull request <https://github.com/ilovetux/unitils/pulls>`_

EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to become feature-compatible with watch
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

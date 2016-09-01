pawn.py(1)
**********

Name
====

   pawn.py - Pattern scanning and processing language based on Python and awk.

SYNOPSIS
========

.. code:: bash

   pawn.py [OPTIONS] SCRIPT FILE

DESCRIPTION
===========

    Pawn is a language used to scan and process text files based loosely
    on AWK and Python. A Pawn script consists of patterns and actions
    patterns are regular expressions that will be tested against each line
    in the file. If the regular expression is found to match, then the action
    associated with the pattern will be executed.

    An action is defined as a block of Python code within curly-braces "{}".
    An action has access to three global variables: LINE, FIELDS and FS.
    LINE is the current line which matched the associated pattern, FIELDS
    is a list containing each field which was extracted from LINE based
    on FS or the field seperator (defaults to any whitespace).

    The default pattern matches all lines. The default action will print the
    line.

    This is currently extremely limited compared to the GNU ls command,
    but improvements are expected to be done soon. If you need a specific
    feature to be completed please don't hesitate to open an issue in
    our `issue tracker <https://github.com/ilovetux/unitils>`_.

OPTIONS
=======

.. code::

    -h, --help
        Prints a usage message and exits

EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to develop features which our users find
interesting and/or useful.

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

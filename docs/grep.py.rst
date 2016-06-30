grep.py(1)
**********

Name
====

   grep.py - print lines matching a pattern

SYNOPSIS
========

.. code:: bash
   grep.py [OPTIONS] PATTERN [FILE...]

DESCRIPTION
===========

    grep.py searches the named input FILEs for lines containing a match to the
    given PATTERN. If no files are specified, or if the file "-" is given,
    grep.py searches standard input. By default, grep.py prints the matching
    lines.

    This is a simplified clone of the well-known grep command. Not all options
    for the original will be available for this command. In addition, regular
    expressions are handled differently by grep.py than by grep. Particularly
    only one flavor of regular expressions are supported, this is because
    Python's regular expression is used for ease and speed of development.

OPTIONS
=======

Generic Program Information
---------------------------

.. code::

    --help
        Output a usage message and exits.
    -V, --version
        Output the version number of grep.py and exit

Matching Control
-----------------

.. code::

    -i, --ignore-case
        Ignore case distinctions in both the PATTERN and the input files.
    -v, --invert-match
        Invert the sense of matching, to select non-matching lines

General Output Control
----------------------

.. code::

    --color[=WHEN]
        WHEN can be "never", "always" or "auto".  On *nix systems, ANSI escape
        sequences are used to achieve terminal coloring. On Windows systems,
        these ANSI escape sequences are intercepted and the appropriate system
        API calls are made to color the text. No environment variables are
        interpreted to control the color.

Output Line Prefix Control
--------------------------

.. code::

    -H, --with-filename
        Print the filename for each match.
    -n, --line-number
        Prefix each line of output with a 1-based line number within
        its input file.

EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to become feature-compatible with grep
as released by the Free Software Foundation with the exception of the multiple
regular expression engines. We will stick to Python's native regular expression
engine as we believe that writing regular expression engines is beyond the
scopeof this project.

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
`issue tracker <https://github.com/ilovetux/unitils>`_. This is also the
correct place for feature requests.

SEE ALSO
========

None yet

NOTES
=====

None yet

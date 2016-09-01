wc.py(1)
**********

Name
====

   wc.py - Print newline, word and byte counts for each file

SYNOPSIS
========

.. code:: bash

   wc.py [OPTIONS...] [FILES...]

DESCRIPTION
===========

    Print newline, word and byte counts for each FILE, and a total line
    if more than one file is specified. A word is a non-zero-length sequence
    of characters delimited by whitespace.

    With no FILE or when FILE is "-", read standard input.

    The options below may be used to select which counts are printed, always
    in the following order: newline, word, character, byte, maximum line length.

.. code::

    -c, --bytes
        print the byte counts

    -m, --chars
        print the character counts

    -l, --lines
        print the newline counts

    -L, --max-line-length
        print the maximum display width

    -w, --words
        print the word counts

    -h, --help display this help and exit

    --version
          output version information and exit


EXAMPLES
========

OVERVIEW
========

This is a work-in-progress, we aim to become feature-compatible with wc
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

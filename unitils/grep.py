from __future__ import unicode_literals
import io
import os
import re
import sys
import atexit
import colorama

def magenta(text):
    """Return text surrounded by control characters to turn it magenta
    """
    return "{}{}{}".format(colorama.Fore.MAGENTA, text, colorama.Fore.RESET)

def green(text):
    """Return text surrounded by control characters to turn it green
    """
    return "{}{}{}".format(colorama.Fore.GREEN, text, colorama.Fore.RESET)

def red(text):
    """Return text surrounded by control characters to turn it red
    """
    return "{}{}{}".format(colorama.Fore.RED, text, colorama.Fore.RESET)

def build_regex(pattern, ignore_case):
    flags = re.IGNORECASE if ignore_case else 0
    try:
        return re.compile(pattern, flags=flags)
    except ValueError:
        # Might already be a compiled regular expression
        return re.compile(pattern.pattern, flags=flags)

# Python 2 and 3 compatibility
def is_string(s):
    return isinstance(s, ("".__class__, u"".__class__))

def grep(expr,
         files,
         line_numbers=False,
         filenames=False,
         color=False,
         invert_match=False,
         ignore_case=False):
    """search the contents of files for expr, yield the results

    files can be a filename as str, a list of filenames, a file-like
    object or a list of file-like objects. In any case, all files
    will be searched line-by-line for any lines which contain expr
    which will be yielded.

    This does not support sending text in directly to search, the
    reason is that this operation is fairly simple in Python::

        import re

        expr = re.compile(r"^\d+\s\w+")
        matches = (l for l in text.splitlines() if expr.search(line))
        for line in matching_lines:
            print(line)

    :param files: files to search for expr
    :param expr: the regular expression to search for
    :param line_numbers: If True, line numbers will be prepended to results
    :param filenames: If True, filenames will be prepended to results
    :type filenames: bool
    :type line_numbers: bool
    :type expr: str, compiled regex
    :type files: str, list, file
    """
    expr = build_regex(expr, ignore_case)
    files = files if isinstance(files, list) else [files]
    for index, fp in enumerate(list(files)):
        if is_string(fp) and os.path.exists(fp) and os.path.isfile(fp):
            files[index] = io.open(fp)
            atexit.register(files[index].close)
    for fp in files:
        for line_number, line in enumerate(fp, start=1):
            if bool(expr.search(line)) == invert_match:
                continue
            line = expr.sub(red(r"\g<0>"), line) if color else line
            if line_numbers:
                line = "{}: {}".format(green(line_number) if color else line_number, line)
            if filenames:
                if hasattr(fp, "name"):
                    line = "{}: {}".format(magenta(fp.name) if color else fp.name, line)
                else:
                    line = "{}: {}".format(magenta("<stdin>") if color else "<stdin>", line)
            yield line

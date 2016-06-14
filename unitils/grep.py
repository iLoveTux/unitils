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

def grep(expr,
         files,
         line_numbers=False,
         filenames=False,
         color=False,
         invert_match=False):
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
    if isinstance(expr, str):
        # Compile the str into a regex object, otherwise
        # assume that expr can be used directly, expr should
        # have at least two methods, `search` and `sub`
        expr = re.compile(expr)
    if not isinstance(files, list):
        files = [files]
    for index, fp in enumerate(list(files)):
        if isinstance(fp, str):
            # If fp is a string, assume it is the path to a file,
            # open it and register its "closer" to execute on exit
            files[index] = open(fp, "r", encoding="utf-8")
            atexit.register(files[index].close)
    for fp in files:
        for index, line in enumerate(fp):
            ret = line
            line_number, filename = str(index+1), fp.name
            if bool(expr.search(ret)) != invert_match:
                if color:
                    line_number, filename = green(line_number), magenta(filename)
                    if not invert_match:
                        ret = expr.sub(red(r"\g<0>"), ret)
                if line_numbers:
                    ret = "{}: {}".format(line_number, ret)
                if filenames:
                    ret = "{}: {}".format(filename, ret)
                yield ret

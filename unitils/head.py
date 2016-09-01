import io
import atexit
import itertools

def head(files, lines=10, verbose=False, quiet=False):
    """Read the first 10 lines (by default) of each file in files.

    As this is supposed to imitate the behavior of head, but also
    be used as a Python callable, some liberties have been taken
    to accomodate the functionality.

    If one file is passed in, a generator is returned which will
    yield the first n lines in the file.

    If more than one file is passed in, a dict is returned keyed
    by filename mapping to a generator which will yield the first
    n lines of that file.

    :param files: The files to examine
    :param lines: The number of lines to yield from each file
    :param verbose: Always include the filename (as described above)
    :param quiet: Never include the filename (as described above)
    :type files: str list
    :type lines: int
    :type verbose: boolean
    :type quiet: boolean
    """
    if not isinstance(files, list):
        files = [files]
    for index, file in enumerate(list(files)):
        if isinstance(file, str):
            files[index] = io.open(file, "r")
            atexit.register(files[index].close)
    if len(files) == 1 and verbose is False:
        return (line for i, line in enumerate(files[0]) if i + 1 <= lines)
    ret = {}
    for file in files:
        ret[file.name] = (line for i, line in enumerate(file) if i + 1 <= lines)
    if quiet:
        return itertools.chain.from_iterable(ret.values())
    return ret

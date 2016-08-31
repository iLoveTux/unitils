import io
import atexit
import itertools
def head(files, lines=10, verbose=False, quiet=False):
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

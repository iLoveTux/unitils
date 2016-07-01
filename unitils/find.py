import fnmatch
import stat
import re
import os


def find(path=".", name=None, iname=None, ftype="*"):
    """Search for files in a directory heirarchy.

    This is dramatically different from the GNU version of
    find. There is no Domain Specific language.

    :param path: The directory to start in
    :param name: The name spec (glob pattern) to search for
    :param iname: The case-insensitive name spec (glob pattern) to search for
    :param ftype: The type of file to search for must be one of b, c, d, p, f, k, s or *
    :param ftype: str
    :type iname: str
    :type name: str
    :type path: str
    """
    if ftype not in "bcdpfls*" or len(ftype) != 1:
        raise NotImplementedError(
            "Introspection for {} not implemented".format(ftype)
        )
    ftype_mapping = {
        "b": stat.S_ISBLK, "c": stat.S_ISCHR,
        "d": stat.S_ISDIR, "p": stat.S_ISFIFO,
        "f": stat.S_ISREG, "l": stat.S_ISLNK,
        "s": stat.S_ISSOCK,
        "*": lambda *args, **kwargs: True,
    }
    type_test = ftype_mapping[ftype]

    if name is not None:
        regex = re.compile(fnmatch.translate(name))
    elif iname is not None:
        regex = re.compile(fnmatch.translate(iname), flags=re.IGNORECASE)
    else:
        regex = re.compile(fnmatch.translate("*"))

    if regex.match(path) and type_test(os.stat(path).st_mode):
        yield os.path.relpath(path)

    for root, dirs, files in os.walk(path):
        for n in files + dirs:
            filename = os.path.join(root, n)
            _stat = os.stat(filename)
            if regex.match(n) and type_test(_stat.st_mode):
                yield filename

import os

def which(cmd, _all=False):
    """Search the PATH for the first occurance of cmd.

    :param cmd: The command for which to search
    :param _all: If True, all occurances of cmd on the PATH will be returned
    :type cmd: str
    :type _all: boolean
    """
    PATH = os.environ["PATH"].split(os.pathsep)
    if _all:
        return (os.path.join(path, cmd) for path in PATH
                    if os.path.exists(os.path.join(path, cmd))
                    and os.access(os.path.join(path, cmd), os.X_OK))
    else:
        for path in PATH:
            fname = os.path.join(path, cmd)
            if os.path.exists(fname) and os.access(fname, os.X_OK):
                return fname

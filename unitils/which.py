import os

def which(cmd, _all=False):
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
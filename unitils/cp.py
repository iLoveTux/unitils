import os
import shutil

def cp(src, dst, no_clobber=False, recursive=False):
    if no_clobber and os.path.exists(dst) and os.path.isfile(dst):
        return None
    if recursive:
        return shutil.copytree(src=src, dst=dst)
    return shutil.copy(src=src, dst=dst)

import os
import shutil

def cp(src, dst, no_clobber=False, recursive=False):
    """Copy src to dst.

    :param src: The file(s) to copy
    :param dst: The destination for src
    :param no_clobber: If True, do not overwrite files if they already exist
    :param recursive: If True recursively copy the contents of src to dst
    :type src: str
    :type dst: str
    :type no_clobber: boolean
    :type recursive: boolean
    """
    if no_clobber and os.path.exists(dst) and os.path.isfile(dst):
        return None
    if recursive:
        return shutil.copytree(src=src, dst=dst)
    return shutil.copy(src=src, dst=dst)

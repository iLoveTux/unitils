import shutil

def mv(src, dst):
    """Move or rename src to dst.

    :param src: The file/directory to move
    :param dst: The destination for the files to be moved
    :type src: str
    :param dst: str
    """
    shutil.move(src=src, dst=dst)

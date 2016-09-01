import os

def ls(path=".", _all=False, almost_all=False):
    """Iterator yielding information about path (defaults to
    current directory)

    Currently this will only list the contents of a directory.
    More features will be added in the near future, but if there
    is a certain feature you are in need of, please don't hesitate
    to submit an issue in our
    `issue tracker <https://github.com/ilovetux/unitils/issues>`_
    or better yet submit a
    `pull request <https://github.com/ilovetux/unitils/pulls>`_

    :param path: The directory to list
    :param _all: If True files starting with "." are not ignored
    :param almost_all: Like _all, but do not include "." and ".."
    :type path: str
    :type _all: boolean
    :type almost_all: boolean
    """
    listing = sorted(os.listdir(path))
    if _all:
        listing = [".", ".."] + listing
    elif almost_all:
        pass
    else:
        listing = filter(lambda x: not x.startswith("."), listing)
    for item in listing:
        yield item

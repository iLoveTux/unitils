import os

def ls(path=".", _all=False, almost_all=False):
    listing = sorted(os.listdir(path))
    if _all:
        listing = [".", ".."] + listing
    elif almost_all:
        pass
    else:
        listing = filter(lambda x: not x.startswith("."), listing)
    for item in listing:
        yield item

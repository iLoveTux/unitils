def cat(files, number=False):
    """iterate through each file in files and yield each line
    in turn. If number is True, yield a two-tuple of
    (line_number, line)
    """
    line_number = 1
    for fp in files:
        for line in fp:
            yield (line_number, line) if number else line
            line_number += 1

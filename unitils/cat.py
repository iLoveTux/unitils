def cat(files, number=False):
    """iterate through each file in files and yield each line in turn.

    :param files: The files to concatenate
    :param number: If True, yield two-tuples of (line_number, line)

    :type files: list of open file-like objects
    :type number: boolean
    """
    line_number = 1
    for fp in files:
        for line in fp:
            yield (line_number, line) if number else line
            line_number += 1

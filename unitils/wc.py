import os
import re
import atexit

word = re.compile(r"(.*?)\s+")

def _examine_fp(fp):
    """Examine fp and returns the interesting metrics.

    :param fp: The file-like object to examine
    :type fp: file
    :returns: tuple containing number of lines, words, bytes, chars, max_line_length and filename
    :rtype: tuple
    """
    max_line_length         = 0
    current_lines           = 0
    current_chars           = 0
    current_words           = 0
    current_bytes           = 0
    for line in fp:
        current_lines += 1
        current_words += len(word.findall(line))
        current_chars += len(line)
        current_line_length = len(line.strip())
        if max_line_length < current_line_length:
            max_line_length = current_line_length
    fp.seek(0, os.SEEK_END)
    filename = fp.name if hasattr(fp, "name") else "<stdin>"
    return (
        current_lines,
        current_words,
        fp.tell(),
        current_chars,
        max_line_length,
        filename
    )

def _gather_output(counts,
                  lines,
                  byte_count,
                  chars,
                  words,
                  max_line_length):
    """Takes all available metrics and returns information filtered to reflect user
    options.

    :param counts: The actual measurments returned by _examine_fp(fp)
    :param lines: Whether to include line counts
    :param byte_count: Whether to include bytes count
    :param chars: Whether to include chars count
    :param words: Whether to include word count
    :param max_line_lenth: Whether to include max_line_length

    :type max_line_lenth: boolean
    :type words: boolean
    :type chars: boolean
    :type byte_count: boolean
    :type lines: boolean
    :type counts: tuple
    """
    current_lines           = counts[0]
    current_words           = counts[1]
    current_bytes           = counts[2]
    current_chars           = counts[3]
    current_max_line_length = counts[4]
    current_name            = counts[5]
    if not any((lines, byte_count, chars, words, max_line_length)):
        return (current_lines, current_words, current_bytes, current_name)
    else:
        ret = (current_name, )
        if max_line_length:
            ret = (current_max_line_length,) + ret
        if byte_count:
            ret = (current_bytes,) + ret
        if chars:
            ret = (current_chars,) + ret
        if words:
            ret = (current_words,) + ret
        if lines:
            ret = (current_lines,) + ret
        return ret


def wc(files,
       lines=False,
       byte_count=False,
       chars=False,
       words=False,
       max_line_length=False):
    """Yields newline, word and byte counts for each file and a total
    line if more than one file is specified

    :param files: An iterable of open, file-like objects or strings containing filenames
    :param lines: Whether to include line counts
    :param byte_count: Whether to include bytes count
    :param chars: Whether to include chars count
    :param words: Whether to include word count
    :param max_line_lenth: Whether to include max_line_length

    :type max_line_lenth: boolean
    :type words: boolean
    :type chars: boolean
    :type byte_count: boolean
    :type lines: boolean
    :type files: iterable
    """
    total_lines       = 0
    total_bytes       = 0
    total_chars       = 0
    total_words       = 0
    total_line_length = 0

    for fp in files:
        current_stats = _examine_fp(fp)
        yield _gather_output(current_stats,
                             lines,
                             byte_count,
                             chars,
                             words,
                             max_line_length)

        total_lines += current_stats[0]
        total_words += current_stats[1]
        total_bytes += current_stats[2]
        total_chars += current_stats[3]
        if total_line_length < current_stats[4]:
            total_line_length = current_stats[4]
    if len(files) > 1:
        yield _gather_output(
            (
                total_lines,       total_words,
                total_bytes,       total_chars,
                total_line_length, "total"
            ),
            lines,
            byte_count,
            chars,
            words,
            max_line_length
        )

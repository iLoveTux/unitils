import os
import re
import atexit

def wc(files,
       lines=None,
       byte_count=None,
       chars=None,
       words=None,
       max_line_length=None):
    """Yields newline, word and byte counts for each file and a total
    line if more than one file is specified
    """
    totals = {
        "lines": 0,
        "words": 0,
        "bytes": 0,
        "chars": 0,
        "longest_line": 0,
        "name": "total"
    }
    word = re.compile(r"(.*?)\s+")
    fps = []
    for f in files:
        if isinstance(f, str):
            fp = open(f, "rb")
            fps.append(fp)
            atexit.register(fp.close)
        else:
            fps.append(f)
    for fp in fps:
        ret = {
            "words": 0,
            "lines": 0,
            "bytes": os.path.getsize(fp.name),
            "chars": 0,
            "name": fp.name
        }

        longest_line = 0
        for index, line in enumerate(fp):
            _words = word.findall(line.decode("utf-8"))
            ret["lines"] += 1
            ret["words"] += len(_words)
            ret["chars"] += len(line)
            _length = len(line.strip())
            longest_line = _length if _length > longest_line else longest_line

        totals["words"] += ret["words"]
        totals["lines"] += ret["lines"]
        totals["bytes"] += ret["bytes"]
        totals["chars"] += ret["chars"]
        if longest_line > totals["longest_line"]:
            totals["longest_line"] = longest_line

        if not any((lines, byte_count, chars, words, max_line_length)):
            yield (ret["lines"], ret["words"], ret["bytes"], ret["name"])
        else:
            _ret = (ret["name"],)
            if max_line_length:
                _ret = (longest_line, *_ret)
            if byte_count:
                _ret = (ret["bytes"], *_ret)
            if chars:
                _ret = (ret["chars"], *_ret)
            if words:
                _ret = (ret["words"], *_ret)
            if lines:
                _ret = (ret["lines"], *_ret)
            yield _ret
    if len(files) > 1:
        if not any((lines, byte_count, chars, words, max_line_length)):
            yield (totals["lines"], totals["words"], totals["bytes"], totals["name"])
        else:
            _ret = (totals["name"],)
            if max_line_length:
                _ret = (longest_line, *_ret)
            if byte_count:
                _ret = (totals["bytes"], *_ret)
            if chars:
                _ret = (totals["chars"], *_ret)
            if words:
                _ret = (totals["words"], *_ret)
            if lines:
                _ret = (totals["lines"], *_ret)
            yield _ret

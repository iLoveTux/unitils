import sys
import unitils
import argparse
import colorama; colorama.init()

def grep(argv=None):
    """search for patterns of text in a set of files.

    :param argv: The list of args to be parsed as options (defaults to sys.argv[1:])
    :type argv: list
    """
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="grep.py",
        description="A simplistic grep-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "--line-number", "-n", action="store_true",
        help="If specified, line numbers will be prepended to the output"
    )
    parser.add_argument(
        "--with-filename", "-H", action="store_true",
        help="If specified, filenames will be prepended to the output"
    )
    parser.add_argument(
        "--invert-match", "-v", action="store_true",
        help="If specified, non-matching lines will be printed"
    )
    parser.add_argument(
        "--color", choices=["auto", "never"], default="auto",
        help="When to add color to output, when 'auto' (default) output"
             "will be colored as long as the output is not to a file "
             "when 'never' no color will be added."
    )
    parser.add_argument(
        "expr",
        help="The regular expression for which to search"
    )
    parser.add_argument(
        "files", nargs="*", default=[sys.stdin],
        help="The file(s) to search for expr"
    )
    args = parser.parse_args(argv)
    kwargs = {
        "expr": args.expr,
        "files": args.files,
        "line_numbers": args.line_number,
        "filenames": args.with_filename,
        "invert_match": args.invert_match,
        "color": args.color == "auto"
    }
    for line in unitils.grep(**kwargs):
        print(line.rstrip())

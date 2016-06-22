from __future__ import print_function
import sys
import unitils
import argparse
import colorama; colorama.init()

def cat(argv, output_stream=sys.stdout):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="wc.py",
        description="A Simplified wc-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "files", nargs="*", default=[sys.stdin], type=argparse.FileType("rb"),
        help="A list of files to inspect"
    )
    parser.add_argument(
        "--number", "-n", action="store_true",
        help="number all output lines"
    )
    args = parser.parse_args(argv)
    kwargs = {
        "files": args.files,
        "number": args.number
    }
    for line in unitils.cat(**kwargs):
        if isinstance(line, tuple):
            output_stream.write("\t{}  {}".format(*line))
        else:
            output_stream.write(line)

def wc(argv):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="wc.py",
        description="A Simplified wc-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "files", nargs="*", default=[sys.stdin],
        help="A list of files to inspect"
    )
    parser.add_argument(
        "--bytes", "-c", action="store_true",
        help="Print the bytes count"
    )
    parser.add_argument(
        "--chars", "-m", action="store_true",
        help="Print the characters count"
    )
    parser.add_argument(
        "--lines", "-l", action="store_true",
        help="Print the newline count"
    )
    parser.add_argument(
        "--max-line-length", "-L", action="store_true",
        help="Print the bytes count"
    )
    parser.add_argument(
        "--words", "-w", action="store_true",
        help="Print the word count"
    )
    args = parser.parse_args(argv)
    kwargs = {
        "files": args.files,
        "lines": args.lines,
        "byte_count": args.bytes,
        "chars": args.chars,
        "words": args.words,
        "max_line_length": args.max_line_length
    }
    for result in unitils.wc(**kwargs):
        print(result)


def find(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="find.py",
        description="A Simplified find-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "path", nargs="?", default=".",
        help="The path to search, defaults to current directory"
    )
    parser.add_argument(
        "-iname", nargs="?", default=None,
        help="The case-insensitive name spec (glob pattern) to search for"
    )
    parser.add_argument(
        "-name", nargs="?", default=None,
        help="The case-sensitive name spec (glob pattern) to search for"
    )
    parser.add_argument(
        "-type", nargs="?", default="*",
        choices=("b", "c", "d", "p", "f", "l", "s"),
        help="The file type to search for [bcdpfls]"
    )
    args = parser.parse_args(argv)
    kwargs = {
        "path": args.path,
        "iname": args.iname,
        "name": args.name,
        "ftype": args.type
    }
    for result in unitils.find(**kwargs):
        print(result)

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
        "--ignore-case", "-i", action="store_true",
        help="If specified, lines will be matched without regard to case"
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
        "ignore_case": args.ignore_case,
        "color": args.color == "auto"
    }
    for line in unitils.grep(**kwargs):
        print(line.rstrip())

from __future__ import print_function, unicode_literals
from __future__ import print_function
import os
import sys
import unitils
import argparse
from itertools import cycle
from .util import get_terminal_size
from time import time, ctime
import colorama; colorama.init()

def mv(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="mv.py",
        description="A Simplified mv-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument("src", help="The file or directory to move")
    parser.add_argument("dst", help="The destination for src")
    args = parser.parse_args(argv)
    kwargs = {
        "src": args.src,
        "dst": args.dst
    }
    unitils.mv(**kwargs)


def head(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="head.py",
        description="A Simplified head-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument("-n", "--lines", type=int, default=10,
                        help="The number of lines to print")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Do not print header with filename")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Always print header with filename")
    parser.add_argument("files", nargs=argparse.REMAINDER,
                        help="The file(s) which to examine")
    args = parser.parse_args(argv)
    kwargs = {
        "files": args.files,
        "lines": args.lines,
        "quiet": args.quiet,
        "verbose": args.verbose
    }
    results = unitils.head(**kwargs)
    if isinstance(results, dict):
        for filename, lines in results.items():
            out.write("==> {} <==\n".format(filename))
            for line in lines:
                out.write(line)
    else:
        for line in results:
            out.write(line)

def cp(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="cp.py",
        description="A Simplified cp-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument("-R", "--recursive",
                        action="store_true",
                        help="If specified, src will be copied "
                             "recursively to dst")
    parser.add_argument("-n", "--no-clobber",
                        action="store_true",
                        help="If specified, src will not be copied "
                             "if it already exists")
    parser.add_argument("src", help="file to copy")
    parser.add_argument("dst", help="destination of copy")
    args = parser.parse_args(argv)
    kwargs = {
        "src": args.src,
        "dst": args.dst,
        "recursive": args.recursive,
        "no_clobber": args.no_clobber
    }
    unitils.cp(**kwargs)


def which(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="which.py",
        description="A Simplified which-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "cmd",
        help="The executable for which to search PATH"
    )
    parser.add_argument(
        "-a", "--all", action="store_true",
        help="If specified, print all locations of cmd on PATH"
    )
    args = parser.parse_args(argv)
    kwargs = {
        "cmd": args.cmd,
        "_all": args.all,
    }
    if not args.all:
        out.write(unitils.which(**kwargs)+"\n")
    else:
        for location in unitils.which(**kwargs):
            out.write(location+"\n")


def watch(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="watch.py",
        description="A Simplified watch-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "command",
        help="command to monitor"
    )
    parser.add_argument(
        "--interval", "-n", type=int, default=2,
        help="seconds to wait between updates"
    )
    args = parser.parse_args(argv)
    kwargs = {
        "command": args.command,
        "interval": args.interval
    }
    terminal_width = unitils.get_terminal_size()[0]
    try:
        for out, err, rc in unitils.watch(**kwargs):
            msg = "every {} seconds: {}".format(args.interval, args.command)
            timestamp = ctime(time())
            header = "{}{}{}".format(
                msg,
                " " * (terminal_width-(len(msg)+len(timestamp))),
                timestamp
            )
            clear()
            print(header, end="\n\n")
            print(out.decode("utf-8"))
    except KeyboardInterrupt:
        pass

def ls(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="ls.py",
        description="A Simplified ls-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "path", nargs="?", default=".",
        help="list information about path (defaults to current directory)"
    )
    parser.add_argument(
        "--all", "-a", action="store_true",
        help="If specified, do not ignore 'dot files'"
    )
    parser.add_argument(
        "--almost-all", "-A", action="store_true",
        help="Do not list '.' and '..'"
    )
    args = parser.parse_args(argv)
    kwargs = {
        "path": args.path,
        "_all": args.all,
        "almost_all": args.almost_all
    }
    output = sorted(list(unitils.ls(**kwargs)), key=lambda s: s.lower())
    width = get_terminal_size()[0]
    num_rows = 1
    while True:
        rows = [list() for row in range(num_rows)]
        for index, row in enumerate(cycle(rows)):
            try:
                row.append(output[index])
            except IndexError:
                break
        widths = []
        for index in range(len(rows[0])):
            widths.append(len(max([row[index] for row in rows], key=len)) + 2)
        if sum(widths) > width:
            num_rows += 1
        else:
            for row in rows:
                for index, item in enumerate(row):
                    fmt_str = "{:<%s}" % str(widths[index])
                    out.write(fmt_str.format(item))
                out.write("\n")
            break
            

def cat(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="cat.py",
        description="A Simplified cat-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "files", nargs="*", default=[sys.stdin], type=argparse.FileType("r"),
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
            out.write("\t{}  {}".format(*line))
        else:
            out.write(line)

def wc(argv=None, out=sys.stdout, err=sys.stderr):
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(
        prog="wc.py",
        description="A Simplified wc-like utility",
        epilog="Copyright 2016 iLoveTux - all rights reserved"
    )
    parser.add_argument(
        "files", nargs="*", default=[sys.stdin], type=argparse.FileType("r"),
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
    fmt_str = ""
    rows = list(unitils.wc(**kwargs))
    widths = []
    for index in range(len(rows[0])):
        widths.append(len(max([str(row[index]) for row in rows], key=len)) + 2)
    for row in rows:
        for index, item in enumerate(row[:-1]):
            fmt_str = "{:>%s}" % widths[index]
            out.write(fmt_str.format(item))
        fmt_str = " {:<%s}" % widths[-1]
        out.write(fmt_str.format(row[-1]) + "\n")


def find(argv=None, out=sys.stdout, err=sys.stderr):
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
        result = u"{}{}".format(result, os.linesep)
        out.write(result)

def grep(argv=None, out=sys.stdout, err=sys.stderr):
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
        out.write(line)

#!/usr/bin/python3
""".
# author: s.giger
# description: compare files in directories.
# ===========================================================
"""

import argparse
import sys
import logging
import os
import datetime
from filecmp import dircmp

RC = 0  # Returncode


# Parsing Script Arguments
parser = argparse.ArgumentParser(
    description='This script compares files in two directories.')
parser.add_argument(
    'dir1', help='path/to/dir1 for the operation (default: current dir = {})'
    .format(os.getcwd()), nargs='?', type=str, default=os.getcwd())
parser.add_argument(
    'dir2', help='path/to/dir2 for the operation', type=str)
parser.add_argument(
    '-f', '--forced', help='forced mode will do compare, regardless of yyy',
    action="store_true")
parser.add_argument(
    '--version', action='version', version='%(prog)s 2.0')
group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
group.add_argument(
    "-q", "--quiet", help="opposite of verbosity",
    action="store_true")
group.add_argument(
    '-v', '--verbosity', help="increase output verbosity",
    action="count", default=0)

args = parser.parse_args()


# ===========================================================
def compare(dir1, dir2):
    """Compare directories: dir1 with dir2."""
    try:
        global RC
        verbalize(
            "verbose",
            "increased verbosity level: %s" % args.verbosity)

        verbalize(
            "'%s' compared to '%s'." % (dir1, dir2),
            "Comparing (using dircmp) '%s' to '%s'" % (dir1, dir2))

        if args.quiet:
            pass
        elif args.verbosity >= 2:
            dircmp(dir1, dir2).report_full_closure()
        elif args.verbosity >= 1:
            dircmp(dir1, dir2).report_partial_closure()
        else:
            print_diff_files(dircmp(dir1, dir2))

    except Exception as e:
        logging.warning(e)
        print(e)
        RC = e.errno
        sys.exit(RC)
    finally:
        logging.info(
            "Script END: %s. Completion Code: %s", datetime.datetime.now(), RC)


# ===========================================================
# verbosity level influences processing messages...
def verbalize(shortmsg, longmsg):
    """Print given message, depending on verbosity."""
    if args.quiet:
        pass
    elif args.verbosity >= 2:
        print(longmsg)
    elif args.verbosity >= 1:
        print(shortmsg)


def print_diff_files(dcmp):
    """ Compare Directories given as dircmp object."""
    if dcmp.diff_files:  # differing content of common files
        for name in dcmp.diff_files:
            print("Directory Compare: differing file %s found in %s and %s"
                  % (name, dcmp.left, dcmp.right))
    elif dcmp.left_only:  # files only in original directory
        for name in dcmp.left_only:
            print("Directory Compare: file %s found only in %s and not in %s"
                  % (name, dcmp.left, dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)


compare(args.dir1, args.dir2)

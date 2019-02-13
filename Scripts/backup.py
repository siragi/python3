#!/usr/bin/python3
""".
# author: s.giger
# description: copy files to a backup store.
# ===========================================================
"""

import argparse
import sys
import logging
import shutil
import os
import datetime
from io import UnsupportedOperation
from builtins import FileNotFoundError, FileExistsError, PermissionError

logging.basicConfig(filename='backup.log', level=logging.DEBUG)
log = logging.getLogger("BackupLog")
log.info("Script BEGIN: %s", datetime.datetime.now())
# logging.warning('I print to stderr by default')
# logging.info('For this you must change the level and add a handler.')

# Errorcodes not yet used as return codes
# Most Errorcodes delivered by sys.exit will use module errno
# (used by exception class)
E_UNSUPPORTEDOP = 4
E_OTHERERR = 99
RC = 0  # Returncode
# ===========================================================
# Parsing Script Arguments
parser = argparse.ArgumentParser(
    description='This script copies files to a backup store.')
parser.add_argument(
    'infile', help='path/to/input for the operation (default: stdin)',
    type=str, default=sys.stdin)
parser.add_argument(
    'outfile', help='path/to/output for the operation (defaultdir: backup)',
    nargs='?', type=str, default="backup")
parser.add_argument(
    '-f', '--forced', help='forced mode will do backup, regardless of yyy',
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
def filebackup(src, dst):
    """Backup."""
    verbalize(
        "'%s', backup: '%s'." % (src, dst),
        "Backing up '%s' to '%s' with permissions and timestamps"
        % (src, dst))
    shutil.copy2(src, dst)


def copytree(src, dst, symlinks=False, ignore=None):
    """
    Correctly copy an entire directory.

    :param src: source dir
    :param dst: destination dir
    :param symlinks: copy content of symlinks
    :param ignore: ignore
    """
    verbalize(
        "'%s', backup: '%s'." % (src, dst),
        "Backing up (using copy2 and copytree) '%s' to '%s' with permissions and timestamps"
        % (src, dst))
    # List Files in directory
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):  # Copy directories
            shutil.copytree(s, d, symlinks, ignore)
        else:                 # Copy files
            shutil.copy2(s, d)


def process(i, o):
    """Process invokes filebackup."""
    try:
        verbalize(
            "verbose",
            "increased verbosity level: %s" % args.verbosity)
        # filebackup(i, o)
        copytree(i, o, symlinks=False, ignore=None)
    # except FileNotFoundError as e:
    #     log.warning(e)
    #     sys.exit(e.errno)
    # except PermissionError as e:
    #     log.warning(e)
    #     sys.exit(e.errno)
    # except FileExistsError as e:
    #     log.warning(e)
    #     sys.exit(e.errno)
    # except UnsupportedOperation as e:
    #     log.warning(e)
    #     sys.exit(e.errno)
    # except OSError as e:
    #     log.warning(e)
    #     sys.exit(e.errno)
    except Exception as e:
        log.warning(e)
        global RC
        RC = e.errno
        sys.exit(e.errno)
    finally:
        log.info(
            "Script END: %s. Completion Code: %s", datetime.datetime.now(), RC)
        verbalize(
            "RC: %s" % RC, "Completion Code: %s. Consult 'backup.log' if RC not 0: Contains datetime and Errors." % RC)


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


process(args.infile, args.outfile)

# if args.verbosity >= 2:
#     print("verbosity level is: %s" % args.verbosity)
#     print("Backing up '%s' into '%s' with permissions and timestamps"
#           % (args.infile, args.outfile))
# elif args.verbosity >= 1:
#     print("verbose")
#     print("Backing up '%s' into '%s'."
#           % (args.infile, args.outfile))
# else:
#     print("silence")

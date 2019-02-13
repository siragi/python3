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
from filecmp import dircmp

BACKUP_LOG = '/documents/backup/backup.log'
MAIN_BACKUP_DIR_fmt = '/documents/backup/local/{}/{}'
EXTERNAL_DRIVE_DIRECTORY_fmt = '/documents/backup/externaldrive/backup_{}'
RC = 0  # Returncode


def _get_date():
    """Return datetime string yyyy-mm-dd_hh:mm."""
    return datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')


# Setting up a logger to write to BACKUP_LOG
logging.basicConfig(filename=BACKUP_LOG, level=logging.DEBUG)
log = logging.getLogger("BackupLog")
log.info("Script START: %s", _get_date())


# ===========================================================


def get_backup_directory(
        base_dir_fmt=MAIN_BACKUP_DIR_fmt, src_dir=os.path.abspath(os.curdir)):
    """.
    Replace 'base_dir/{}/{}'                     (using string.format)
         to 'base_dir/src_dir/yyyy-mm-dd_hh:mm'. (default src_dir=curdir)
    """
    backup_directory = base_dir_fmt.format(
        os.path.basename(src_dir), _get_date())
    return backup_directory


# Parsing Script Arguments
parser = argparse.ArgumentParser(
    description='This script copies files to a backup store.')
parser.add_argument(
    'indir', help='path/to/input for the operation (default: current dir= {})'
    .format(os.getcwd()),
    nargs='?', type=str, default=os.getcwd())
parser.add_argument(
    'outdir', help='path/to/output for the operation (defaultdir: {})'
    .format(get_backup_directory()),
    nargs='?', type=str, default=get_backup_directory())
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


def process(i, o):
    """Process invokes filebackup."""
    try:
        global RC
        verbalize(
            "verbose",
            "increased verbosity level: %s" % args.verbosity)
        # filebackup(i, o)
        verbalize(
            "'%s', backup: '%s'." % (i, o),
            "Backing up (using copytree) '%s' to '%s' \
            with permissions and timestamps"
            % (i, o))
        shutil.copytree(i, o, symlinks=False, ignore=None)
    except shutil.Error as e:
        errors = e.args[0]
        for error in errors:
            _, _, msg = error
            log.warning(msg)
            print(msg)
            RC = int(msg.split(']')[0].split()[1])  # split "[Errno XX] desc"
            print()
        sys.exit(RC)
    except Exception as e:
        log.warning(e)
        print(e)
        RC = e.errno
        sys.exit(RC)
    finally:
        log.info("Script END: %s. Completion Code: %s", _get_date(), RC)
        print_diff_files(dircmp(i, o))
        verbalize(
            "RC: %s. Details: 'backup.log'" % RC,
            "Completion Code: %s. Consult 'backup.log' if RC not 0: \
            Contains datetime and Errors." % RC)


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

process(args.indir, args.outdir)

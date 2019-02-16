#!/usr/bin/python3
# author: s.giger
# ===========================================================

import argparse
import sys
import logging
# import shutil
from io import UnsupportedOperation
from builtins import FileNotFoundError, FileExistsError, PermissionError

# Errorcodes no more used as return codes
E_BADARGS = 85
E_NOFILE = 86
E_NOPERM = 2
E_FILEEXISTS = 3
E_UNSUPPORTEDOP = 4
E_OTHERERR = 99


# logging.warning('I print to stderr by default')
# logging.info('For this you must change the level and add a handler.')


# ===========================================================
# Parsing Script Arguments
parser = argparse.ArgumentParser(
    description='This script allows you to do xxx with a file..')
parser.add_argument(
    'infile', help='path/to/inputfile for the operation (default: stdin)',
    type=str, default=sys.stdin)
parser.add_argument(
    'outfile', help='path/to/outputfile for the operation (default: stdout)',
    nargs='?', type=str, default=sys.stdout)
parser.add_argument(
    '-f', '--forced', help='forced mode will do xxx, regardless of yyy',
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
# Check if file argument is a file and set processingFile if true
# if os.path.isfile(args.infile):
#     processingFile = args.infile
# else:
#     processingFile = None

if args.infile:
    processingFile = args.infile
else:
    processingFile = ''
# ===========================================================
# The process itself


def openfile(filename, modus):
    # use it within a exception handler
    with open(filename, modus) as f:
        print("processing open file {}".format(filename))
        # print(f.readlines())
        # oder:
        # cont = file.read()
        # print(cont)
        # f.close() is integrated in with statement.


def process(filename, modus):
    try:
        openfile(filename, modus)
    except FileNotFoundError as e:
        logging.warning("I did not find filename '%s'!", filename)
        return e.errno
    except PermissionError as e:
        logging.warning(
            "Permission denied to open '%s' in '%s' mode.", filename, modus)
        return e.errno
    except FileExistsError as e:
        logging.warning("File '%s' already exists", filename)
        return e.errno
    except UnsupportedOperation as UsO:
        logging.warning(
            "UnsupportedOperation: %s in '%s' mode", str(UsO), modus)
        return UsO.errno
    except IOError as e:
        logging.warning("I/O Error occurred: %s", str(IOError))
        return e.errno
    finally:
        print("Will be printed in the end, whatever happens.")


# ===========================================================


def main():
    """Start."""
    # verbosity level influences processing messages...
    if args.verbosity >= 2:
        print("verbosity level is: %s" % args.verbosity)
        # Process file if set
        if processingFile:
            print("'%s' is a file and will be processed" % args.infile)
            rcp = process(processingFile, 'r')
        else:
            print("'%s' is not a file to be processed" % args.infile)
    elif args.verbosity >= 1:
        print("verbose")
        # Process file if set
        if processingFile:
            print("Processing '%s'" % args.infile)
            rcp = process(processingFile, 'r')
        else:
            print("'%s' no file" % args.infile)
    else:
        print("silence")
        if processingFile:
            rcp = process(processingFile, 'r')
    return rcp


if __name__ == "__main__":
    # Some exceptions in main() return integer as Returncode, some not (None)
    try:
        rc = int(main())
    except TypeError:
        print("Exception without standard Errno occured: rc=1 instead.")
        rc = 1
    sys.exit(rc)

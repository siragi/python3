#!/usr/bin/python3
# author: s.giger
# ===========================================================

import argparse
import sys
import logging
# import shutil
from io import UnsupportedOperation
from builtins import FileNotFoundError, FileExistsError, PermissionError

# Errorcodes not yet used as return codes
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
    except FileNotFoundError:
        logging.warning("I did not find filename '%s'!" % filename)
        sys.exit(E_NOFILE)
    except PermissionError:
        logging.warning(
            "Permission denied to open '%s' in '%s' mode." % (filename, modus))
        sys.exit(E_NOPERM)
    except FileExistsError:
        logging.warning("File '%s' already exists" % filename)
        sys.exit(E_FILEEXISTS)
    except UnsupportedOperation as UsO:
        logging.warning(
            "UnsupportedOperation: %s in '%s' mode" % (str(UsO), modus))
        sys.exit(E_UNSUPPORTEDOP)
    except IOError:
        logging.warning("I/O Error occurred: %s" % str(IOError))
        sys.exit(E_OTHERERR)
    finally:
        print("Will be printed in the end, whatever happens.")


# ===========================================================
# verbosity level influences processing messages...
if args.verbosity >= 2:
    print("verbosity level is: %s" % args.verbosity)
    # Process file if set
    if processingFile:
        print("'%s' is a file and will be processed" % args.infile)
        process(processingFile, 'r')
    else:
        print("'%s' is not a file to be processed" % args.infile)
elif args.verbosity >= 1:
    print("verbose")
    # Process file if set
    if processingFile:
        print("Processing '%s'" % args.infile)
        process(processingFile, 'r')
    else:
        print("'%s' no file" % args.infile)
else:
    print("silence")
    if processingFile:
        process(processingFile, 'r')

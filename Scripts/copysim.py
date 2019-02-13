#!/usr/bin/python3
from shutil import copyfile
from sys import argv
from os.path import isfile

basename = __file__


def usage():
    print(
        """
        Usage: %s source destination

        This copies a File.

        PARAMETERS:
        ===========
        source: /path/to/source
        destination: /path/to/destination""" % basename)


def check_copy():
    if isfile(argv[2]):
        print("Copy worked!")
    else:
        print("Copy not worked!")


try:
    if len(argv) == 3:
        if isfile(argv[1]):
            if not isfile(argv[2]):
                copyfile(argv[1], argv[2])
                check_copy()
            else:
                print("%s exists allready!" % argv[2])
        else:
            print("%s doesn't exist!" % argv[1])

    else:
        usage()
except PermissionError:
    print("Permission denied!")
except:
    print("An error occurred")
    raise
# except * as Error:   (Code NOK)
#     print ("Another Error than PermissionError occurred: ")
#     print (dir(Error))

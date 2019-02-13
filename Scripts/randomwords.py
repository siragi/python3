#!/usr/bin/python3
"""Return a random word from a dictionary file."""
import random
import sys
import os


def usage():
    basename = __file__
    usage = """
Usage: %s [<mydict>]

This script returns a random word from a dictionary file.

PARAMETERS:
===========
<mydict>: /path/to/dictionary. (Default:/usr/share/dict/words)""" % basename
    print(usage)


if len(sys.argv) == 1:
    sDictName = "/usr/share/dict/words"
elif os.path.isfile(sys.argv[1]):
    sDictName = sys.argv[1]
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    usage()
    exit(0)
else:
    print("Could not use given argument %s as dictionary." % sys.argv[1])
    usage()
    exit(2)
with open(sDictName, "r") as fDict:
    w1 = fDict.readlines()
    print("There are %d words in the dictionary %s" % (len(w1), sDictName))
    wordnum = random.randint(0, len(w1)-1)
    word = w1[wordnum].strip()
    print("I chose word number %d, which is \"%s\"" % (wordnum+1, word))

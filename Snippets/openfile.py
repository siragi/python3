#!/usr/bin/python3
from io import UnsupportedOperation
# import errno
from builtins import FileNotFoundError, FileExistsError, PermissionError

filename = "testtest"
modus = "r"
"""
r - (default mode) open the file for reading
w - open the file for writing, overwriting the content \
    if the file already exists with data
x - creates a new file, failing if it exists
a - open the file for writing, appending new data at the end \
    of the file's contents if it already exists
b - write binary data to files instead of the default text data
+ - allow reading and writing to a mode
"""

try:
    with open(filename, modus) as f:
        if modus == 'r':
            print(f.read())
        elif modus == 'w':
            f.write("some test text\ntdriaentriaen\ndtiranetriaen\n")
            # print(f.read())
        # f.close() is integrated in with statement.
except FileNotFoundError:
    print("I did not find filename '%s'!" % filename)
except PermissionError:
    print("Permission denied to open '%s' in '%s' mode." % (filename, modus))
except FileExistsError as e:
    print(e)
    print("-> File '%s' already exists. Is opening mode '%s' ok?"
          % (e.filename, modus))
except UnsupportedOperation as UsO:
    print("UnsupportedOperation: %s in '%s' mode" % (str(UsO), modus))
# except OSError as e:
#     print("IOError occurred for file operaton with '%s' in '%s' mode:"
#           % (filename, modus))
#     print("-> %s" % e)
#     if e.errno == errno.EACCES:
#         print("   '%s' has no access. Use chmod or the like" % e.filename)
#     if e.errno == errno.EEXIST:
#         print("   '%s' already exists. Is opening mode '%s' ok?"
#               % (e.filename, modus))
finally:
    print("Will be printed in the end, whatever happens.")

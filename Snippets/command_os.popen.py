# (DEPRICATED) source: https://stackabuse.com/pythons-os-and-subprocess-popen-commands/
# not recommended for py3, i guess!
import os

p = os.popen('ls -la')
print(p.read())


# os.popen2 python2 only!!!
#
# This method is very similar to the previous one. The main difference is what the method outputs. In this case it returns two file objects, one for the stdin and another file for the stdout.

# The syntax is as follows:

# popen2(cmd[, mode[, bufsize]])
#
# These arguments have the same meaning as in the previous method, os.popen.
in2, out2 = os.popen2('ls -l')
print(out2.read())

in3, out3, err3 = os.popen3('ls -la')
print(out3.read())

import subprocess
# import logging
#


# recommended:
def run_ls_lisa():
    """Run ls -lisa and give output as string."""
    ls = subprocess.run(
        ["ls", "-lisa"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8")
    lsout = ls.stdout  # one big string <class 'str'>
    return lsout


lsopen = subprocess.Popen(
    ["ls", "-lisa"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    encoding="utf-8")
lspout = lsopen.stdout.readlines()  # a list of lines

for line in lspout:
    print(line, end="")
print("2--------")

# The available parameters are as follows:
# subprocess.Popen(
#     args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)

# not correctly closing yet:
subprocess.Popen('ls -la', shell=True)
print("3--------")
# If shell is True, the specified command will be executed through the shell. This can be useful if you are using Python primarily for the enhanced control flow it offers over most system shells and still want convenient access to other shell features such as shell pipes, filename wildcards, environment variable expansion, and expansion of ~ to a user’s home directory. However, note that Python itself offers implementations of many shell-like features (in particular, glob, fnmatch, os.walk(), os.path.expandvars(), os.path.expanduser(), and shutil).


# Popen objects are supported as context managers via the with statement: on exit, standard file descriptors are closed, and the process is waited for.
# source: https://docs.python.org/3/library/subprocess.html
with subprocess.Popen(["ls"], stdout=subprocess.PIPE) as proc:
    print(proc.stdout.read())  # bytes as output: b'file1\n...fileX\n'
    # If encoding or errors are specified, or text (also known as universal_newlines) is true, the file objects stdin, stdout and stderr will be opened in text mode using the encoding and errors specified in the call or the defaults for io.TextIOWrapper.
    # If text mode is not used, stdin, stdout and stderr will be opened as binary streams. No encoding or line ending conversion is performed.
print("3.2--------")


with subprocess.Popen(
    'ls -la', shell=True, stdout=subprocess.PIPE, encoding="utf-8") as p:

    for line in p.stdout.readlines():
        print(line, end='')
print("3.3--------")


def shellresponselist(shellcommand):
    """Store shellcommand response elegantly in a list."""
    with subprocess.Popen(shellcommand, shell=True, stdout=subprocess.PIPE,
                          encoding="utf-8") as p:
        responselines = [
            line.rstrip() for line in p.stdout.readlines()
            ]
    return responselines


def pipedresponse():
    p1 = subprocess.Popen(
        'ls -lisa', shell=True, stdin=None, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    p2 = subprocess.Popen('grep -i "test"', shell=True, stdin=p1.stdout)

    p1.stdout.close()
    out, err = p2.communicate()
    return (out, err)

# start excel on windows: (good to know)
# subprocess.Popen("start excel", shell=True)
# equivalent to:
# subprocess.Popen("C:\Program Files (x86)\Microsoft Office\Office15\excel.exe")


def main():
    """Choose Function by uncommenting."""
    funclist = [
        run_ls_lisa,
        pipedresponse,
        ]

    for f in funclist:
        print(f.__name__, "\n *************", f())

    # uncomment, or adapt Function
    print("shellresponselist()")
    for i in shellresponselist('ls -lisa'):
        print(i)


if __name__ == '__main__':
    main()

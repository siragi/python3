"""Extract a Zipfile."""
from zipfile import ZipFile, BadZipFile, LargeZipFile
import os
import sys
import datetime

zipfile = "demoö.zip"
# zipfile = "bad.zip"
# zipfile = "large.zip"
files2zip = "zip_plz"
newzipfile = "demo3.zip"


def get_paths(directory):
    """Give back recursive filepaths (tree) of all files in given directory."""
    paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)
    return paths


def extractZip(ziparchive):
    """Extract all files of given ziparchive in the current directory."""
    try:
        # ZipFile constructor; READ mode; ZipFile object named as zipf
        with ZipFile(ziparchive, 'r') as zipf:
            # To print contents of the archive
            zipf.printdir()

            # Extract contents of the ZIP to the current working directory,
            # ! overwriting existing files
            print("Extracting files")
            zipf.extractall()
            print("Finished extracting")
    except BadZipFile as e:
        print(e)
    except LargeZipFile as e:
        # When a Python ZIPfile needs ZIP64 functionality,
        # but it hasn’t been enabled, Python throws this exception.
        print(e)


def createZip(src, dest):
    """Create ziparchive with source (recursively) to dest ziparchive."""
    try:
        paths = get_paths(src)
        print("Zipping these files to {}:".format(dest))
        for file in paths:
            print(file)
        # ZipFile constructor, write mode
        with ZipFile(dest, 'w') as zipf:
            for file in paths:
                zipf.write(file)
        print("Zip successful")
    except (FileExistsError, FileNotFoundError, PermissionError) as e:
        print(e)


def getZipinfo(ziparchive):
    """Print ziparchive properties (modtime, system, zipversion, bytes)."""
    with ZipFile(ziparchive, 'r') as zipf:
        for info in zipf.infolist():
            print(info.filename)
            print('\tModified:\t'+str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t'+str(info.create_system)+'(0=Windows,3=Unix)')
            print('\tZIP version:\t'+str(info.create_version))
            print('\tCompressed:\t'+str(info.compress_size)+' bytes')
            print('\tUncompressed:\t'+str(info.file_size)+' bytes')


def testrun():
    """No Action, if comments are not gone."""
    try:
        os.chdir("../path/to/dir")
        # extractZip(zipfile)
        # createZip(files2zip, newzipfile)
        getZipinfo(zipfile)
        pass
    except (FileExistsError, FileNotFoundError, PermissionError) as e:
        print(e)
        return e.errno
    except Exception as e:
        print(e)
        return e.errno


if __name__ == "__main__":
    try:
        rc = int(testrun())
    except TypeError:
        print("Exception without standard Errno occured: rc=1 instead.")
        rc = 1
    sys.exit(rc)

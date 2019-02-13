"""Extract a Zipfile."""
from zipfile import ZipFile, BadZipFile, LargeZipFile
import os


zipfile = "demo.zip"
# zipfile = "bad.zip"
# zipfile = "large.zip"
files2zip = "zip_plz"
newzipfile = "demo2.zip"


def get_paths(directory):
    paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)
    return paths


def extractZip(file):
    try:
        # ZipFile constructor; READ mode; ZipFile object named as zipf
        with ZipFile(file, 'r') as zipf:
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
        # When a Python ZIPfile needs ZIP64 functionality, but it hasn’t been enabled, Python throws this exception.
        print(e)


def createZip(src, dest):
    try:
        paths = get_paths(src)
        print("Zipping these files:")
        for file in paths:
            print(file)
        # ZipFile constructor, write mode
        with ZipFile(dest, 'w') as zipf:
            for file in paths:
                zipf.write(file)
        print("Zip successful")
    except (FileExistsError, FileNotFoundError, PermissionError) as e:
        print(e)


# Run
try:
    os.chdir("../path/to/dir")
    # extractZip(zipfile)
    createZip(files2zip, newzipfile)
except Exception as e:
    print(e)
    raise

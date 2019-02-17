# see https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/


def shortandinteresting():
    """Open file and read the content in a list. Short, less understandable."""
    with open('testtest', 'r') as filehandle:
        contentlist = [
            line.rstrip() for line in filehandle.readlines()
            ]
    return contentlist

# above is equivalent to:


def longbutnice():
    """Open file and read the content in a list (longer code, but easy)."""
    contentlist = []
    with open('testtest', 'r') as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            item = line[:-1]

            # add item to the list
            contentlist.append(item)
    return contentlist


print(shortandinteresting())

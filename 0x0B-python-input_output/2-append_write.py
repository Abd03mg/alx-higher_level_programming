#!/usr/bin/python3
''' Append to file. '''


def write_file(filename="", text=""):
    ''' function that writes string to file.
    Args:
        filename: name of file to be written.
        text: text to be written.
    Return:
        number of chars has been written.
    '''
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)

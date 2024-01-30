#!/usr/bin/python3
def read_file(filename=""):
    ''' Function that reads file and prints it to stdout.
        Args:
            filename: name of file to be read.
    '''
    with open(filename, "r", encoding="utf-8") as f:
        for _ in f:
            print("{:s}".format(_), end="")

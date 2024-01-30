#!/usr/bin/python3
''' Module contains function that uses to read text file. '''


def read_file(filename=""):
    ''' Function that reads file and prints it to stdout.
        Args:
            filename: name of file to be read.
    '''
    with open(filename, "r", encoding="utf-8") as f:
        for _ in f:
            print("{:s}".format(_), end="")

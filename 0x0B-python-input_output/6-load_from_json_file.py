#!/usr/bin/python3
''' Load from JSON file '''


def load_from_json_file(filename):
    ''' function that load from json file.
    Args:
        filename: name of file to be loaded.
    Return:
        python object.
    '''
    load = __import__("json").load
    with open(filename) as f:
        return load(f)

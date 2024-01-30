#!/usr/bin/python3
''' From JSON string to object'''


def to_json_string(my_str):
    ''' function that convert from json to object.
    Args:
        my_object: input JSON string.
    Return:
        python object.
    '''
    load = __import__("json").loads
    return (load(my_str))

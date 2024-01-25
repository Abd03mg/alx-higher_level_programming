#!/usr/bin/python3
""" function that returns a list of all attributes of object."""


def lookup(object):
    """look up function.
    Args:
        object: input object.
    Return:
        list of object attr.
    """
    return (dir(object))

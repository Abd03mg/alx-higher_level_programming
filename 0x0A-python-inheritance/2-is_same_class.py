#!/usr/bin/python3
''' Exact same object  '''


def is_same_class(obj, a_class):
    ''' function that check is inctance of class.
    Args:
        obj: object to be cheked.
        a_class: ...
    Return:
        True if smame class, otherwise False.
    '''
    return (type(obj) == a_class)

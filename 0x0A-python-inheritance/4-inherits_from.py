#!/usr/bin/python3
''' Only sub class of '''


def inherits_from(obj, a_class):
    ''' Is subclass.
    Args:
        obj: ...
        a_class: ...
    Return:
        .....
    '''
    return (issubclass(type(obj), a_class) and type(obj) != a_class)

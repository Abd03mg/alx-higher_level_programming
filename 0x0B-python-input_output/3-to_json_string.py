#!/usr/bin/python3
''' To JSON string '''


def to_json_string(my_obj):
    ''' function that convert to json.
    Args:
        my_object: input object.
    Return:
        json type.
    '''
    dump = __import__("json").dumps
    return (dump(my_obj))

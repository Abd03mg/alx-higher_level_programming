#!/usr/bin/python3
''' Save To JSON file '''


def save_to_json_file(my_obj, filename):
    ''' function that writes to json file
    Args:
        filename: name of file to be wriiten.
        my_object: input object.
    Return:
        json respr.
    Expect:
        return expection if the object can't be serialized.
    '''
    dump = __import__("json").dump
    with open(filename, "w+", encoding="utf-8") as f:
        dump(my_obj, f)

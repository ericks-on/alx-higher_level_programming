#!/usr/bin/python3
"""this module contains function that serializes using json
"""


import json


def to_json_string(my_obj):
    """this function returns JSON rep of object passed

    Args:
        my_obj: object to serialize

    Return:
        string: the JSON representation of the object

    """
    r = json.dumps(my_obj)
    return (r)

#!/usr/bin/python3
"""module contains one function which creates an object from a json file

"""


import json


def load_from_json_file(filename):
    """this function creates object from a JSON file

    Attributes:
        obj_str: json string rep of object
        the_obj: the object finally deserialized

    Args:
        filename(string): the name of the file

    """
    with open(filename, encoding='utf-8') as f:
        obj_str = f.read()
        the_obj = json.loads(obj_str)
        return (the_obj)

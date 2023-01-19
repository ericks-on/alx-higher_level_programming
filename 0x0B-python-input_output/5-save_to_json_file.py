#!/usr/bin/python3
"""this module contains one function which saves object to file
"""


import json


def save_to_json_file(my_obj, filename):
    """this function saves an object in json rep to file

    Args:
        my_obj: object to save
        filename(string): name of the file

    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

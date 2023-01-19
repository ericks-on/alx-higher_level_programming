#!/usr/bin/python3
"""module contains oly one function using json
"""

def from_json_string(my_str):
    """this function returns an object rep by a JSON string

    Args:
        my_str: JSON representation of an object

    Return:
        object that is represented by my_str

    """
    r = json.loads(my_str)
    return (r)

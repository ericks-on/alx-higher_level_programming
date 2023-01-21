#!/usr/bin/python3
"""this module contains task 8 for 0x0B
"""


def class_to_json(obj):
    """this function returns the dictionary description with simple data
    structre

    Args:
        obj: an instance of a class

    Returns:
        the dictionary description with simple data description

    """
    return (obj.__dict__)

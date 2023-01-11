#!/usr/bin/python3
"""module contains first task in the inheritance project"""
def lookup(obj):
    """function returns list of available attributes and methods
    of an object

    Args:
        obj: object to get available attributes and methods

    Return:
        list: list of all available attributes and methods of the object
        
    """
    return (dir(obj))

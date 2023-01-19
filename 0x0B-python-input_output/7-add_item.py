#!/usr/bin/python3
"""module is a script to add all arguments to a python list, and save them to afile

Attributes:
    save: function to save object string rep to file
    load: function to load object from file

"""

import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def create_list():
    """this function creates list and adds arguments to it
    
    Attributes:
        the_list: the list to add arguments
        l: length of argv
        args: argument vector

    Returns:
        list: a list containing all arguments already appended

    """
    the_list = []
    if len(sys.argv) > 1:
        args = sys.argv
        l = len(sys.argv)
        for n in range(1, l):
            the_list.append(args[n])
    return (the_list)


def main():
    """this is the main

    Attributes:
        obj: the object to add to file
        filename: name of the file

    """
    obj = create_list()
    filename = 'add_item.json'
    save(obj, filename)


main()

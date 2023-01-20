#!/usr/bin/python3
"""module is a script to add all arguments to a python list, and save them to afile

Attributes:
    save: function to save object string rep to file
    load: function to load object from file

"""

import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def add_to_list():
    """this function creates list and adds arguments to it
    
    Attributes:
        the_list: the list to add arguments
        l: length of argv
        args: argument vector
        filename: name of file
        f: object contained in json file

    Returns:
        list: a list containing all arguments already appended

    """
    filename = 'add_item.json'
    f = open(filename, 'a+', encoding='utf-8')
    f.seek(0)
    if len(f.read()) == 0:
        the_list = []
        f.close()
    else:
        the_list = load(filename)
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
    obj = add_to_list()
    filename = 'add_item.json'
    save(obj, filename)


main()

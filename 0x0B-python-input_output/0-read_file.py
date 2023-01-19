#!/usr/bin/python3
"""module contains function that reads a text file

"""
def read_file(filename=""):
    """this function reads contents of a file and prints it to stdout

    Args:
        filename: the name of the file 

    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())

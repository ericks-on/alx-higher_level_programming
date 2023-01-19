#!/usr/bin/python3
"""contains function to append contents in a file

"""


def append_write(filename="", text=""):
    """this function appends text at the end of a file
    Attributes:
        n: the number of characters that are written to file

    Args:
        filename(string): the name of the file
        text(string): text to add to file

    Returns:
        int: the number of characters written to file

    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))

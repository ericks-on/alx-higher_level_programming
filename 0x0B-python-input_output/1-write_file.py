#!/usr/bin/python3
"""module contains a function used to write contents in atext file

"""


def write_file(filename="", text=""):
    """this function uses write call to write to file
    
    Attributes:
        n(int): number of characters written

    Args:
        filename(string): the name of the file
        text(string): the text to write on file

    Returns:
        int: the number of characters written

    """
    with open(filename, 'w', encoding='utf-8') as f:
        n = f.write(text)
    return (n)

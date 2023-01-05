#!/usr/bin/python3
"""module to modify the rectangle class by adding width and
height
"""
class Rectangle:
    """adds two private instance variables height and width
    also defines functions to set and fetch the variables
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    def width(self):
        """getter of __width

        Return:
            __width: shorter side of the rectangle

        """
        return (self.__width)
    def width(self, value):
        """setter of __width

        Args:
            value(int): the value to set

        Attributes:
            __width:horizontal dimension

        Raises:
        TypeError: if the value is not an integer
        ValueError: if the value is less than or equal to  0
        """
        if isinstance(value, int) is True:
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
    def height(self):
        """getter of height

        Return:
            __height:vertical dimension

        """
        return (self.__height)
    def height(self, value):
        """setter of height

        Args:
            value:value to set

        Attributes:
            __height:vertical dimension

        Raises:
        TypeError: if value is not an integer
        ValueError: if value isless or equal to 0

        """
        if isinstance(value, int) is True:
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

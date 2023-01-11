#!/usr/bin/python3
"""second task in inheritance project of creating a class"""
class MyList(list):
    """class has methods that operate on list

    """
    def print_sorted(self):
        """this function prints list sorted in ascending order

        Attributes:
            cpy: this is a copy of the list

        """
        cpy = MyList(self)
        cpy.sort()
        print("{}".format(cpy))

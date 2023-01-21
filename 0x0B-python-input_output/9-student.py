#!/usr/bin/python3
"""This module contains task 9 for project 0x0B
"""


class Student:
    """This class defines a student

    The __init__ method initializes the first name, last name and age of the
    student

    Args:
        first_name: the first name of the student
        last_name: last name of the student
        age: age of the student

    Attributes:
        first_name: first name of the student
        last_name: last name of the student
        age: age of the student

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method retrieves a dictionary representation of a Student class
        instance

        Returns:
            The dictionary representation of Student instance

        """
        return (self.__dict__)

#!/usr/bin/python3
"""This module contains task 11 for project 0x0B
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

    def to_json(self, attrs=None):
        """This method retrieves a dictionary representation of a Student class
        instance

        Attributes:
            new_dict: dictionary containing attributes in attrs

        Returns:
            only attributes in attrs list if listed otherwise all attributes

        """
        if attrs:
            new_dict = {}
            for k in attrs:
                # check if attribute exists in the class
                if k in (self.__dict__).keys():
                    new_dict[k] = (self.__dict__)[k]
            return (new_dict)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """This method replaces all of the Student instance

        Args:
            json: dictionary containing the attributes to replace

        """
        for key in json.keys():
            # check if key is in class attributes dictionary
            if key in (self.__dict__).keys():
                # change the attribute values
                self.key = json[key]

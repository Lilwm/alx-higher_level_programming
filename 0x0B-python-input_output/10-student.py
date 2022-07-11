#!/usr/bin/python3
"""student to JSON with filters"""


class Student:
    """defines a class student"""

    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dict representation of Student with specified attr"""
        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            new_dict = {}
            for element in attrs:
                if type(element) != str:
                    return self.__dict__
                if element in self.__dict__.keys():
                    new_dict[element] = self.__dict__[element]
            return new_dict

#!/usr/bin/python3
"""represents an object to another format"""


class Student:
    """defines a class"""

    def __init__(self, first_name, last_name, age):
        """initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict representation of Student with specified attr"""
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

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for key in json:
            setattr(self, key, json[key])

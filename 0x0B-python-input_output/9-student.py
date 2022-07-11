#!/usr/bin/python3
""" loads a class to JSON"""


class Student:
    """defines a student class"""

    def __init__(self, first_name, last_name, age):
        """ initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dictionary representation of Student"""
        return self.__dict__

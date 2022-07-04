#!/usr/bin/python3
""" a class that raises exception"""


class BaseGeometry:
    """a class with public attribute ares"""
    def area(self):
        """public instance: raises an exception when called"""
        raise Exception("area() is not implemented")

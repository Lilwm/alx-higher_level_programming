#!/usr/bin/python3
"""checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """ returns true if obj is the exact class, otherwise false"""
    return (type(obj) == a_class)

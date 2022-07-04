#!/usr/bin/python3
""" """


def inherits_from(obj, a_class):
    """ returns True if the object is a subclass otherwise False"""
    return(issubclass(type(obj),a_class) and type(obj) != a_class)

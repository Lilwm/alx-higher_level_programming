#!/usr/bin/python3
""" checks for a subclass """


def inherits_from(obj, a_class):
    """ returns True if the object is a subclass otherwise False"""
    
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True

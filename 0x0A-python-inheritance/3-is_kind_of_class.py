#!/usr/bin/python3
"""  checks for inheritance """


def is_kind_of_class(obj, a_class):
    """ returns true if obj is instance or inherited frm a_class"""
    return (isinstance(obj, a_class))

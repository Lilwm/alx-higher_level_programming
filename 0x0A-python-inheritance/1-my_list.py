#!/usr/bin/python3
""" a class that inherits from list"""


class MyList(list):
    """ a subclass of List"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))

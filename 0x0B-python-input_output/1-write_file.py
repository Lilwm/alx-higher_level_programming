#!/usr/bin/python3
""" write to a file"""


def write_file(filename="", text=""):
    """ writes a string to a text file
    Returns: No of chars written"""
    with open(filename, 'w', encoding="utf-8") as wf:
        return wf.write(text)

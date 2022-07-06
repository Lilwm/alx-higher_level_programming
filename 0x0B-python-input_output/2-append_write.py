#!/usr/bin/python3
""" append write"""


def append_write(filename="", text=""):
    """appends a string to eof and returns count of chars"""
    with open(filename, 'a', encoding="utf-8") as appendfile:
        return appendfile.write(text)

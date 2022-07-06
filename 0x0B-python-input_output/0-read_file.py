#!/usr/bin/python3
""" opens and reads files"""

def read_file(filename=""):
    """opens a file and reads data"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

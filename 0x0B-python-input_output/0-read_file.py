#!/usr/bin/python3

def read_file(filename=""):
    """opens a file and reads data"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

#!/usr/bin/python3
"""a function that creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """returns created file from JSON"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

#!/usr/bin/python3
""" saves an object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file using JSON"""
    with open(filename, 'w', encoding="utf-8") as savefile:
        return json.dump(my_obj, savefile)

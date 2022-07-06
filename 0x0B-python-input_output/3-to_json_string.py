#!/usr/bin/python3
""" to JSON string"""
import json


def to_json_string(my_obj):
    """returns JSON repr of a str my_obj"""
    return json.dumps(my_obj)

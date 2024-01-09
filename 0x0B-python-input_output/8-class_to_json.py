#!/usr/bin/python3
"""
Containing the class_to_json(obj)
"""


def class_to_json(obj):
    """returning the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__

#!/usr/bin/python3
"""
Containing the load_from_file(filename)
"""


import json

def load_from_json_file(filename):
    """creating an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

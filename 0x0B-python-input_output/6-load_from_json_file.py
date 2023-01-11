#!/usr/bin/python3
"""creates an Object from a “JSON file
    """

import json

def load_from_json_file(filename):
    """creates an Object from a “JSON file
    """
    with open(filename, mode="r") as data_file:
        return json.load(data_file)

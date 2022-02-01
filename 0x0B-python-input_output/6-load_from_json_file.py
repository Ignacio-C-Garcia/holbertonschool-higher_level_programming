#!/usr/bin/python3
"""module name"""


import json


def load_from_json_file(filename):
    """name"""
    with open(filename, mode='r', encoding='utf-8') as txto:
        return json.loads(txto.read())

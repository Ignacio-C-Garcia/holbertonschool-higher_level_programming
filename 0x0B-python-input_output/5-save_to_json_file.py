#!/usr/bin/python3
"""module name"""

import json


def save_to_json_file(my_obj, filename):
    """fun name"""
    with open(filename, mode='w', encoding='utf-8') as txt:
        txt.write(json.dumps(my_obj))

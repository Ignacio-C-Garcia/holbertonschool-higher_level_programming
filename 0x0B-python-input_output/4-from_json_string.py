#!/usr/bin/python3
"""name"""


import json


def from_json_string(my_str):
    """apkm"""
    with open(my_str, 'r', encoding='utf-8') as texto:
        return json.dumps(texto.read())

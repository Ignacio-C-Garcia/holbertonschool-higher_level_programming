#!/usr/bin/python3
"""name"""


def write_file(filename="", text=""):
    """name"""
    with open(filename, mode='w', encoding='utf-8') as fd:
        return fd.write(text)

#!/usr/bin/python3
"""name"""


def append_write(filename="", text=""):
    """name"""
    with open(filename, mode='a', encoding='utf-8') as potato:
        return potato.write(text)

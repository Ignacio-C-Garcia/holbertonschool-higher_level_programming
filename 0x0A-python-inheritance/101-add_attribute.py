#!/usr/bin/python3
"""module doc"""


def add_attribute(obj, key, value):
    """add_attribute doc"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)

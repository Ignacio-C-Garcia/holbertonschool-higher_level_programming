#!/usr/bin/python3
"""module"""


def add_attribute(obj, name, value):
    """adentro"""
    if obj.__dict__ == 0:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

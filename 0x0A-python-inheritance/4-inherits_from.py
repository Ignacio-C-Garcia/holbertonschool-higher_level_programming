#!/usr/bin/python3
"""module"""


def inherits_from(obj, a_class):
    """adentro"""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False

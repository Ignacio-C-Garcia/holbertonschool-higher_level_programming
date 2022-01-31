#!/usr/bin/python3
"""module"""


def inherits_from(obj, a_class):
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False

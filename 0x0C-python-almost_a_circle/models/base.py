#!/usr/bin/python3
"""module name"""


class Base:
    """class name"""
    __nb_objects = 0
    def __init__(self, id=None):
        """init"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

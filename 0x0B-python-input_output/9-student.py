#!/usr/bin/python3
"""name"""


class Student:
    """name"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """name"""
    def to_json(self):
        return self.__dict__

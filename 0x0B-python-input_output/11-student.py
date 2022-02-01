#!/usr/bin/python3
"""name"""


class Student:
    """name"""
    def __init__(self, first_name, last_name, age):
        """name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """name"""
        aux = {}
        if type(attrs) == list:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
            for item in set(self.__dict__.keys()) & set(attrs):
                aux.setdefault(item, self.__dict__.get(item))
            return aux
        return self.__dict__

    def reload_from_json(self, json):
        """comment"""
        for item in self.__dict__:
            if item in json:
                self.__dict__[item] = json[item]


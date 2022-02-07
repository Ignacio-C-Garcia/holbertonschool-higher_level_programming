#!/usr/bin/python3
"""module name"""

import json


class Base:
    """class name"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """comment"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """comment"""
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
                return
            aux = []
            for object in list_objs:
                aux.append(cls.to_dictionary(object))
            file.write(cls.to_json_string(aux))

    @staticmethod
    def from_json_string(json_string):
        """comment"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """comment"""
        if cls.__name__ == 'Rectangle':
            aux = cls(1, 1)
            aux.update(**dictionary)
            return aux
        aux = cls(1)
        aux.update(**dictionary)
        return aux

    @classmethod
    def load_from_file(cls):
        """comment"""
        aux = []
        try:
            with open(f'{cls.__name__}.json') as file:
                for line in file:
                    for item in cls.from_json_string(line):
                        aux.append(cls.create(**item))
                return aux
        except Exception:
            return []

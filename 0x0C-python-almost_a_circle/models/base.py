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
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
                return
            aux = []
            for object in list_objs:
                aux.append(cls.to_dictionary(object))
            file.write(cls.to_json_string(aux))

        
        
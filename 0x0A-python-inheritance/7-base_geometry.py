#!/usr/bin/python3
"""module"""


class BaseGeometry():
    """adentro"""
    def area(self):
        """adentro"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """adentro"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

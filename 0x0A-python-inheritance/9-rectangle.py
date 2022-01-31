#!/usr/bin/python3
"""module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """adentro"""
    def __init__(self, width, height):
        """adentro"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """adentro"""
        return self.__width * self.__height

    def __str__(self):
        """adentro"""
        return f'[Rectangle] {self.__width}/{self.__height}'

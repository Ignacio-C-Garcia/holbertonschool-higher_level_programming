#!/usr/bin/python3
"""module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """adentro"""
    def __init__(self, width, height):
        """adentro"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

#!/usr/bin/python3
"""module"""


BaseRectangle = __import__('9-rectangle').Rectangle


class Square(BaseRectangle):
    """text"""
    def __init__(self, size):
        """adentro"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """adentro"""
        return f'[Square] {self.__size}/{self.__size}'

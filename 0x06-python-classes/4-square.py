#!/usr/bin/python3
"""modulo con clase square"""


class Square:
    """atributo size int mayor o igual a 0"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    """methodo area retorna el area del cuadrado"""
    def area(self):
        return self.__size ** 2
    """getter_size"""
    @property
    def size(self):
        return self.__size
    """setter_size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

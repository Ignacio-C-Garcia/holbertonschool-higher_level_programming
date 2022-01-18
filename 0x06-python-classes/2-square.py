#!/usr/bin/python3
""" modulo con clase square"""
class Square:
    """ square tiene un atributo size que debe ser un int mayor o igual a 0"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

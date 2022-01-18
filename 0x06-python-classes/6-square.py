#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position
    """methodo area retorna el area del cuadrado"""
    def area(self):
        return self.__size ** 2
    """getter self"""
    @property
    def size(self):
        return self.__size
    """getter position"""
    @property
    def position(self):
        return self.position
    """setter size"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    """setter position"""
    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
    """print a square of #"""
    def my_print(self):
        if self.__size == 0:
            print()
            return

        for line in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for space in range(self.__position[0]):
                print(' ', end='')
            for y in range(self.__size):
                print('#', end='')
            print()

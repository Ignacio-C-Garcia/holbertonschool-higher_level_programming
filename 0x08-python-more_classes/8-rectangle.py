#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width < 0 or self.height < 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        lstr = ''
        if self.height < 0 or self.width < 0:
            return lstr
        for y in range(self.height):
            for x in range(self.width):
                lstr += f"{getattr(self, 'print_symbol')}"
            if y != self.height - 1:
                lstr += '\n'
        return lstr

    def __repr__(self):
        return f'{type(self).__name__}({self.width}, {self.height})'

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
    @property
    def width(self):
        
        return self.__width
    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise ValueError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise ValueError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

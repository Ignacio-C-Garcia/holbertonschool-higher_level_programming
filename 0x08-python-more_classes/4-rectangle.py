#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width < 0 or self.height < 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        lstr = ''
        for y in range(self.height):
            for x in range(self.width):
                lstr += '#'
            if y != self.height - 1:
                lstr += '\n'
        return lstr

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
#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
                lstr += '#'
            if y != self.height - 1:
                lstr += '\n'
        return lstr

    def __repr__(self):
        return f'{type(self).__name__}({self.width}, {self.height})'

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

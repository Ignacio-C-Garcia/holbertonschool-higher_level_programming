#!/usr/bin/python3
"""module name"""


from models.base import Base


class Rectangle(Base):
    """class name"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """display"""
        for y in range(self.y):
            print()
        for height in range(self.height):
            print(" " * self.x, end='')
            for width in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """str"""
        lstr = f"[{self.__class__.__name__}] "
        lstr += f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return lstr

    def update(self, *args, **kwargs):
        """update"""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                return
        else:
            for attr in kwargs:
                try:
                    getattr(self, attr)
                except Exception as f:
                    return
                setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rdic = {}
        rdic.setdefault("id", self.id)
        rdic.setdefault("width", self.width)
        rdic.setdefault("height", self.height)
        rdic.setdefault("x", self.x)
        rdic.setdefault("y", self.y)
        return rdic

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

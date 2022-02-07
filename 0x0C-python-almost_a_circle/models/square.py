#!/usr/bin/python3
"""module name"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class name"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        lstr = f"[{self.__class__.__name__}] "
        lstr += f"({self.id}) {self.x}/{self.y} - {self.width}"
        return lstr

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update"""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = self.width
                self.x = args[2]
                self.y = args[3]
            except Exception:
                return
        else:
            if "size" in kwargs:
                kwargs.setdefault("width", kwargs["size"])
                kwargs.setdefault("height", kwargs["size"])
                del kwargs["size"]
            for attr in kwargs:
                try:
                    getattr(self, attr)
                except Exception as f:
                    print(f)
                setattr(self, attr, kwargs[attr])

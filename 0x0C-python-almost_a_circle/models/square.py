#!/usr/bin/python3

"""square.py
This module contains a class 'square' that inherits from Base
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class of a square object"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update Square attributes"""
        if args is not None and len(args) > 0:
            keylist = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i < 4:
                    setattr(self, keylist[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

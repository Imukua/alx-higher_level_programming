#!/usr/bin/python3
"""Defines a Square  class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance
           Args:
                :: size(int): Size of the square length and width
                :: x(int): x coordinate
                :: y(int): y coordinate
                :: id(int): idenntity of new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square width/length"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of the square length/width"""

        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square attribute using provided aargument
           Args:
                1. id
                2. size
                3. x
                4. y
            kwargs: Dictionary with key value argument pairs
        """
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
                if len(args) >= 2:
                    self.size = args[1]
                    if len(args) >= 3:
                        self.x = args[2]
                        if len(args) >= 4:
                            self.y = args[3]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.y, self.x)
                    else:
                        self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary rep of the Square object instance"""

        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """Returns the str representation of the square"""

        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

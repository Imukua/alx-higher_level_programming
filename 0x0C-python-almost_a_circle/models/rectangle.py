#!/usr/bin/python3

"""Defines a Rectangle class that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle inhering from class Base
            Args:
                :: width(int): width of the rectangle
                :: heigth(int): height of the rectangle
                :: x: x
                :: y: y
            Raises:
                :: TypeError: if x, y, width, height are not intergers
                :: ValueError: if x, y, width. height are not greater than 0
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get value of attribute - width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set value of attribute - width"""

        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get value of attribute - height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set value of attribute - height"""

        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get value of attribute - x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of attribute - x"""

        if not isinstance(value, int):
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get value of attribute - y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set value of attribute - y"""

        if not isinstance(value, int):
            raise TypeError("y must be an interger")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle instance"""

        return self.height * self.width

    def display(self):
        """Prints the instance of rectangle using #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates a Recangle instance using arguments provided
           Order:
                1. id
                2. width
                3. height
                4. x
                5. y
        """

        if args:
            if len(args) >= 1:
                self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                    if len(args) >= 3:
                        self.height = args[2]
                        if len(args) >= 4:
                            self.x = args[3]
                            if len(args) >= 5:
                                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary rep of the rectangle object instance"""

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

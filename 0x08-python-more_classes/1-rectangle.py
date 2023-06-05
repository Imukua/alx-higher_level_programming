#!/usr/bin/python3

""" Define a class for a rectangle """


class Rectangle:
    """ Definition of the rectange class"""

    def __init__(self, width=0, height=0):
        """ Task:
                 Initialising a new recctangle
            Args:
                 width(int): Variable holding the rect width.
                 height(int): Var holding the rect height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Set or get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Set or get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

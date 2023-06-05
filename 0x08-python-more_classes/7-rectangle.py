#!/usr/bin/python3

""" Define a class for a rectangle """


class Rectangle:
    """ Definition of the rectange class

        Attributes:
        number_of_instances (int): The number of Rectangle instances available.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Task:
                 Initialising a new recctangle
            Args:
                 width(int): Variable holding the rect width.
                 height(int): Var holding the rect height.
        """
        type(self).number_of_instances += 1
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns area of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Returns a string repressentation of the rectangle """

        if self.__width == 0 or self.height == 0:
            return('')
        rectangle = []
        for i in range(self.__height):
            [rectangle.append(self.print_symbol) for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns the string representation of the rectangle."""

        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Prints a message for every deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

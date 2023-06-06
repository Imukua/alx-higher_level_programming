#!/usr/bin/python3

""" Defines a function t print a square """


def print_square(size):
    """ Prints a square made of # character
        args:
            size(int): The size of the square
        raise:
        a. TypeError: if size is not an integer
                      if size is a float < zero
        b. ValueError: if size is < zero
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for length in range(size):
        for width in range(size):
            print('#', end='')
        print()

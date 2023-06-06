#!/usr/bin/python3

""" Defines a Function to add two intrgers """


def add_integer(a, b=98):
    """ Returns a int addition of a and b
        both are casted into int before addition

        raises TypeError for non int or non float values.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

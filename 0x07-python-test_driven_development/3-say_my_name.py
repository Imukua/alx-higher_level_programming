#!/usr/bin/python3

""" Defines a function to print a namw"""


def say_my_name(first_name, last_name=""):
    """ Prints a first and last name
        Raises TypeError if names arent strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

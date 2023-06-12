#!/usr/bin/python3

"""Defines inherited list class MyList."""


class MyList(list):
    """Implement sorted printing for the built-in list class."""

    def print_sorted(self):
        """PrintS a list in sorted ascending order"""
        print(sorted(self))

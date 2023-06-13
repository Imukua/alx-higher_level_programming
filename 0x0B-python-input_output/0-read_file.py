#!/usr/bin/python3

"""Defines a textfile reading function."""


def read_file(filename=""):
    """Prints the context of a UTF8 text file to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

#!/usr/bin/python3
import hidden_4


def printmod():
    varnames = [name for name in dir(hidden_4) if not name.startswith("__")]
    sorted_names = sorted(varnames)
    for name in sorted_names:
        print(name)


if __name__ == "__main__":
    printmod()

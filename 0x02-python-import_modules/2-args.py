#!/usr/bin/python3
from sys import argv


def argprint():
    num = len(argv) - 1
    if num == 1:
        print("1 argument:\n1: {}".format(argv[1]))
    elif num == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(num))
        for i in range(num):
            print("{}: {}".format(i + 1, argv[i + 1]))


if __name__ == "__main__":
    argprint()

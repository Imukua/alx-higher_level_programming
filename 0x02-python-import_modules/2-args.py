#!/usr/bin/python3
from sys import argv


def argprint():
    num = len(argv) - 1
    if num == 1:
        print("1 argument:\n1: {}".format(argv))
    elif num == 0:
        print("0 arguments.")
    else:
        print("{} arguments:\n".format(num))
        count = 1
        for i in range(num):
            print("{}: {}\n".format(count, argv[count]))
            count += 1


if __name__ == "__main__":
    argprint()

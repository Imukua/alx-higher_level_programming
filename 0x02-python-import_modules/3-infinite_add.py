#!/usr/bin/python3
from sys import argv


def addags():
    total = 0
    for i in range(len(argv) - 1):
        total += int(argv[i + 1])
    print(total)


if __name__ == "__main__":
    addags()

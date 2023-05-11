#!/usr/bin/python3

import sys


def calculator():
    if (len(sys.argv) - 1) != 3:
        print(r"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    result = 0

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            print("Error: divisin by zero")
            sys.exit(1)
        result = a / b
    else:
        print("Unknown operator. Available operators: +, -, * and /")

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    calculator()

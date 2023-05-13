#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            print("{:d}".format(elem), end='')
            if elem != row[-1]:
                print(" ", end='')

        print("$")

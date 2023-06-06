#!/usr/bin/python3

""" Define a function for matrix division """


def matrix_divided(matrix, div):
    """ Devides each column for rows in matrix
        Returns a new matrix with the rounded results
        Raises TypeError:
                        a. if matrix isnt list of lists of integers or floats,
                        b. If all rows of the matrix arent the same size,
                        c. div isnt an integer or float,

        Raises ZeroDivisionError:
                        a.If div is equal to 0
    """

    if (not isinstance(matrix, list) and
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    rowsizes = set(len(row) for row in matrix)

    if len(rowsizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)
    return new_matrix

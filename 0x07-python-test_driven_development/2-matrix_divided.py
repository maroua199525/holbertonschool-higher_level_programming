#!/usr/bin/python3
def matrix_divided(matrix, div):
    new = []
    """ function that divides all elements of a matrix.

    Args:
    matrix: a list of lists of integers or floats
    div: integer or float

    Raise:
    matrix must be a list of lists of integers or floats:
    TypeError("matrix must be a matrix (list of lists) 
    of integers/floats")
    TypeError("exception with the message 
    Each row of the matrix must have the same size"
    raise TypeError("div must be a number")
    raise ZeroDivisionError("message division by zero")

    Return : matrix / div
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    x = len(matrix[0])
    for i in range(0, len(matrix)):
        lst = []
        if (len(matrix[i]) != x):
            raise TypeError("Each row of the matrix must \
            have the same size")
        for j in range(0, len(matrix[i])):
            if type(matrix[i]) is not list and type(matrix[i][j])  not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
            lst.append(round((matrix[i][j]/ div), 2))
        new.append(lst)
    return new

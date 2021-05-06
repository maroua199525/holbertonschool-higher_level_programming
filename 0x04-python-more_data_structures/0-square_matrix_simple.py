#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst = []
    new_matrix = []
    length = len(matrix)
    for x in range(0, length):
        lst = list((map(lambda y: y ** 2, matrix[x])))
        new_matrix.append(lst)
    return (new_matrix)

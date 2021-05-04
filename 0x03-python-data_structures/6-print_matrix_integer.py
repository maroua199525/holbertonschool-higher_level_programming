#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(0, length):
        for j in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if not (j == len(matrix[i]) - 1):
                print(end=" ")
        print()

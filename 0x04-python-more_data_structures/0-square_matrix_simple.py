#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for row in range(len(new_matrix)):
        new_matrix[row] = list(map(lambda item: item ** 2, new_matrix[row]))
    return new_matrix

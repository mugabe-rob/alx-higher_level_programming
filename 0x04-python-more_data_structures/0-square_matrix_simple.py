#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for counter in range(len(matrix)):
        new_matrix[counter] = list(map(lambda x: x**2, matrix[counter]))

    return(new_matrix)

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for counter in matrix:
        for column in row:
            print("{:d}".format(column), end=" " if column != row[-1] else "")
        print()

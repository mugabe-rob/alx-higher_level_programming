#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for counter in matrix:
        for column in counter:
            print("{:d}".format(column), end=" " if column != counter[-1] else "")
        print()

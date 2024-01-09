#!/usr/bin/python3
""" Module that returns a list of lists of integers representing Pascal's"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's"""
    my_list = []
    for counter in range(n):
        my_list.append([])
        for j in range(i+1):
            try:
                if j - 1 == -1:
                    my_list[counter].append(1)
                else:
                    my_list[counter].append(my_list[counter-1][j-1] + my_list[counter-1][j])
            except IndexError:
                my_list[counter].append(1)
    return (my_list)

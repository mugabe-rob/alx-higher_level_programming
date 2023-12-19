#!/usr/bin/python3
""" defining a square """


class Square:
    """ A square with private instance attribute size """

    def __init__(self, size=0):
        """
        Args:
            size: The size of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('The size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('The size must be an integer')

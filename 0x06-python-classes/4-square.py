#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Representing a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializing the square
        Args:
            size (int):The size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculating the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): The size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("The size must be an integer")
        else:
            if value < 0:
                raise ValueError("The size must be >= 0")
            else:
                self.__size = value

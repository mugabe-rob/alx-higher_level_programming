#!/usr/bin/python3
"""
10-square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Representing a square.
    Inherits from Rectangle.
    """
    def __init__(self, size):
        """
        init - Initializes a Square.
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area - returning area of a square
        """
        return self.__size ** 2

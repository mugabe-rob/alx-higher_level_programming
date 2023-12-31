#!/usr/bin/python3
"""
8-rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Representing a rectangle.
    Inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializing an instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

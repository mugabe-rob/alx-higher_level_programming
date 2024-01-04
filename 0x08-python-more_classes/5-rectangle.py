#!/usr/bin/python3
"""
Defining a Rectangle class
"""


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initializing """
        self.width = width
        self.height = height

    def __str__(self):
        """ returning set of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += '#'
            ret += '\n'
        return ret[:-1]

    def __repr__(self):
        """ repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del """
        print("Bye rectangle...")

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculating the area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculating the perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

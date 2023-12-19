#!/usr/bin/python3
""" defining a class Square """


class Square:
    """ define __init__ function """
    def __init__(self, size=0):
        """ initializing size of self with size """
        self.size = size

    @property
    def size(self):
        """ returns __size of self """
        return self.__size

    @size.setter
    def size(self, value):
        """ if statement """
        if type(value) is not int:
            """ raise error """
            raise TypeError("The size must be an integer")
        elif value < 0:
            """ raise error """
            raise ValueError("The size must be >= 0")
        else:
            """ initialize """
            self.__size = value
    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
    """ defines my_print function """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for counter in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

#!/usr/bin/python3
"""A class Student that defines a student by:"""


class Student:
    """A class Student that defines a student by:"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for counter in attrs:
                if hasattr(self, counter):
                    my_dict[counter] = getattr(self, counter)
            return my_dict

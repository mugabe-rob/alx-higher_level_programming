#!/usr/bin/python3
"""
containing the Student class
"""

class Student:
    """representing student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """returns a dictionary representation of a student instance with attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            try:
                new_dict[x] = self.__dict__[x]
            except FileNotFoundError:
                pass
            return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for counter in json:
            try:
                setattr(self, counter, json[counter])
            except FileNotFoundError:
                pass

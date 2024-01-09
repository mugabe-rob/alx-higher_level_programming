#!/usr/bin/python3
"""
Containing a class Student
"""

class Student:
    """Instantiation of the student"""
    def __init__(self, first_name, last_name, age):
        """initializing the public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returning a dictionary of students representation"""
        return self.__dict__

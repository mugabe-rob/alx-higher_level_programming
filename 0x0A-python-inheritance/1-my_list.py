#!/usr/bin/python3
"""
containing the MyList class
"""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """printing the sorted list"""
        print(sorted(self))

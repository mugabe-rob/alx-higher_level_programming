#!/usr/bin/python3
"""
Containing the inherit from function
"""



def inherits_from(obj, a_class):
    """returning true if the object is an instance of a class else that false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)

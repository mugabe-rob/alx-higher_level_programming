#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for counter in list(a_dictionary):
        if a_dictionary[counter] == value:
            del a_dictionary[counter]
    return a_dictionary

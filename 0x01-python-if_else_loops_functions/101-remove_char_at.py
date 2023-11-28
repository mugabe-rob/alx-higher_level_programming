#!/usr/bin/python3
def remove_char_at(str, number):
    new = ''
    counter = 0
    for c in str:
        if counter != number:
            new += str[counter]
        counter += 1
    return new

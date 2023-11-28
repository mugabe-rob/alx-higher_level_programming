#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) <= ord('z') and ord(character) >= ord('a'):
            ch = chr(ord(character) - 32)
        else:
            ch = character
        print("{:s}".format(ch), end="")
    print('')

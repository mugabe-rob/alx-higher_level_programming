#!/usr/bin/python3
def multiple_returns(sentence):
    your_tuple = ()
    if len(sentence) == 0:
        your_tuple = 0, "None"
    else:
        your_tuple = len(sentence), sentence[0]
    return your_tuple

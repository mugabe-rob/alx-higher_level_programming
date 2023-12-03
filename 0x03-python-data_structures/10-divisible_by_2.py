#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    your_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            your_list.append(True)
        else:
            your_list.append(False)
    return your_list

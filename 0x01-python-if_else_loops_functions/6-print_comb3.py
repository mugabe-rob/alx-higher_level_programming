#!/usr/bin/python3
for z in range(9):
    for j in range(z + 1, 10):
        if z == 8:
            print("{}{}".format(z, j))
        else:
            print("{}{}".format(z, j), end=", ")

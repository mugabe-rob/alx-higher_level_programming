#!/usr/bin/python3
for a in range(100):
    if a == 99:
        print(a)
    else:
        print("{:0>2d}".format(a), end=", ")

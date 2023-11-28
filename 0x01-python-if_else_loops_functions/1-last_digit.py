#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_dgt = ((number * -1) % 10) * -1
else:
    l_dgt = number % 10
print(f"The Last digit of {number:d} is {last_digit:d} and is", end=" ")
if l_dgt > 5:
    print("It is greater than 5")
elif l_dgt == 0:
    print("0")
else:
    print("It is less than 6 and not 0")

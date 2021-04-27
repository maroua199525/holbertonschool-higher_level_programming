#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    dig = (-1) * (((-1) * number) % 10)
else:
    dig = (number % 10)
if (dig > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, dig))
elif (dig < 6 and dig != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, dig))
elif (dig == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, dig))

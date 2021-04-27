#!/usr/bin/env python3
def uppercase(str):
    i = 0
    while (i < len(str)):
        ch = str[i:i+1]
        i+=1
        k = ord(ch)
        if (k >= 97 and k <= 122):
            k = k - 32
            print("{:c}".format(k), end="")
        else:
            print("{}".format(ch), end="")
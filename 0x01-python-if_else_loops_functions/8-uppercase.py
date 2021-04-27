#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        k = ord(ch)
        if (k >= 97 and k <= 122):
            k = k - 32
        print("{:c}".format(k), end="")
    print("")

#!/usr/bin/env python3
def uppercase(str):
    for ch in str:
        k = ord(ch)
        if (k >= 97 and k <= 122):
            k = k - 32
        print("{}".format(chr(k)), end="")
    print("")

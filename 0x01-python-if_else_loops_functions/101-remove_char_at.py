#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    if n < 0 or n > len(str):
        return str
    for s in str:
        if s != str[n]:
            ch = ch + s
    return ch

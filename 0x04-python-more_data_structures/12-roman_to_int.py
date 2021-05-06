#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or None:
        return (0)
    length = len(roman_string)
    s = 0
    lst = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }
    value = list(lst.values())
    key = list(lst.keys())
    k = 0
    while k < length:
        if k+1 < length and roman_string[k:k+2] in lst:
            s = s + lst[roman_string[k:k+2]]
            k = k+2
        else:
            s = s + lst[roman_string[k]]
            k = k + 1
    return (s)
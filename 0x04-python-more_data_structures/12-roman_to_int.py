#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    if isinstance(roman_string, str) is False:
        return (0)
    length = len(roman_string)
    s = 0
    lst = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }
    value = list(lst.values())
    key = list(lst.keys())
    for k in range(length):
        for i, v in zip(key, value):
            if roman_string[k] == i:
                s = s + v
    return (s)

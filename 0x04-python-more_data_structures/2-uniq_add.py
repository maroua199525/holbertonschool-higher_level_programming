#!/usr/bin/python3
def uniq_add(my_list=[]):
    length = len(my_list)
    new = list(set(my_list))
    s = 0
    for i in new:
        s = s + i
    return (s)

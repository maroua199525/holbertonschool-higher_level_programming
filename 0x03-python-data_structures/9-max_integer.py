#!/usr/bin/python3
def max_integer(my_list=[]):
    len1 = len(my_list)
    max = my_list[0]
    if (len1 == 0):
        return None
    else:
        for i in range(1, len1):
            if my_list[i] > max:
                max = my_list[i]
    return (max)

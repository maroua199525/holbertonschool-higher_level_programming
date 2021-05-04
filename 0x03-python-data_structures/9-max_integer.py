#!/usr/bin/python3
def max_integer(my_list=[]):
    len1 = len(my_list)
    if (len1 == 0):
        return None
    else:
        max = my_list[0]
        for i in range(0, len1):
            if my_list[i] > max:
                max = my_list[i]
    return (max)

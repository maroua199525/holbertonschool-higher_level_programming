#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    len1 = len(my_list)
    for i in range(0, len1):
        if (my_list[i] % 2) == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

#!/usr/bin/python3
def weight_average(my_list=[]):
    len1 = len(my_list)
    if (len1 == 0):
        return (0)
    m = 0
    s = 0
    p = 1
    if (len1 >= 1):
        for i in range(len1):
            for j in range(len(my_list[i]) - 1):
                p = my_list[i][j] * my_list[i][j + 1]
                m = m + my_list[i][j + 1]
            s = s + p
        reslt = (s / m)
    return (reslt)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if (len1 == 0):
        tuple_a = (0, 0)
    elif (len1 == 1):
        tuple_a = (tuple_a[0], 0)
    elif (len2 == 0):
        tuple_b = (0, 0)
    elif (len2 == 1):
        tuple_b = (tuple_b[0], 0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple

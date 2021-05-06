#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary.keys())
    value = a_dictionary.values()
    for i, j in zip(key, value):
        print("{}: {}".format(i, j))

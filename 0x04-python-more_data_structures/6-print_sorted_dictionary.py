#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary.items())
    for i, j in key:
        print("{}: {}".format(i, j))

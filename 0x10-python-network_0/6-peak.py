#!/usr/bin/python3
""" """
def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    if length == 0:
        return None
    for i in range(0, length - 2):
        if (list_of_integers[i] < list_of_integers[i+1] and list_of_integers[i + 1] > list_of_integers[i + 2]):
            return list_of_integers[i + 1]
    return (max(list_of_integers[0], list_of_integers[length - 1]))

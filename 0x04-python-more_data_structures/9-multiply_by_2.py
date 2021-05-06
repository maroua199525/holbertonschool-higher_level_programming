#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = a_dictionary.copy()
    value = list(map(lambda x: x * 2, dictionary.values()))
    key = dictionary.keys()
    for i, v in zip(key, value):
        dictionary[i] = v
    return (dictionary)

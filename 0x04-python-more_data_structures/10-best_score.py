#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary.items()) >= 1:
        score = list((a_dictionary.values()))
        key = list(a_dictionary.keys())
        max = score[0]
        name = key[0]
        for i, v in zip(score, key):
            if i > max:
                max = i
                name = v
        return name

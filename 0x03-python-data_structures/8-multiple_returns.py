#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = ()
    length = len(sentence)
    if length == 0:
        ch = None
    else:
        ch = sentence[0]
    tuple_a = (length, ch)
    return (tuple_a)

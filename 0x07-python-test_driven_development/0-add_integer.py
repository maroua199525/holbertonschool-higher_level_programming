#!/usr/bin/python3
def add_integer(a, b=98):
    """ Addition function

    Args:
    a: integer or float
    b: integer or float

    Raise:
    TypeError(a must be an integer or b must be an integer)

    Return:
    the addition of a and b
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    if (type(a) == float):
        a = int(a)
    if (type(b) == float):
        b = int(b)
    return int(a) + int(b)

#!/usr/bin/python3
""" Module contain function: inherits_from
"""

def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class,
    otherwise False
    """
    if issubclass(a_class, type(obj)):
        return False
    else:
        return issubclass(type(obj), a_class)

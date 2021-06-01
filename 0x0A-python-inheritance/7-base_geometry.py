#!/usr/bin/python3
"""  Module BaseGeometry"""


class BaseGeometry:
    """ class BaseGeometry"""
    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

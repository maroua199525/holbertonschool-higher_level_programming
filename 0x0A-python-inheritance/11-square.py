#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
This module contains Square class that inherits from Rectangle
"""


class Square(Rectangle):
    """ __init__ method """
    def __init__(self, size):
        """
        instantiation
        """

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of the square """
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

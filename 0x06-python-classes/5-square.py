#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """square class defined by size."""
    def __init__(self, size=0):
        """Initializes the private object, sets size to zero"""
        self.__size = size

    @property
    def size(self):
        """ retrieve the value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of __size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return the square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()

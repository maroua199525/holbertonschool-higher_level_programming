#!/usr/bin/python3
class Square:
    """Represents a sequare defines by size."""
    def __init__(self, size=0):
        """Initializes the private object, sets size to zero then
        checks if size has the correct type and the correct value"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ return the square area"""
        return self.__size ** 2

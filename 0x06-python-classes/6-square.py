#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """square class defined by size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the private objectssize and position:
        sets size to zero and position to zero"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ retrieve the value of __size"""
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the value of __position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ return the square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for k in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()

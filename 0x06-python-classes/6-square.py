#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """square class defined by size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the private objectssize and position:
        sets size to zero and position to zero"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """ retrieve the value of __size"""
        """Args: size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of __size"""
        """Args: size of square"""
        """raise: check if value is integer or if value is greater than
        zeor"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Instance method

        return the square area"""
        return self.__size ** 2

    def my_print(self):
        """
        Instance method
        Returns:
            prints in stdout the square with the character #"""
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

    @property
    def position(self):
        """ give the position of the square
            Returns:
            the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of the square
        Args:
            value: (tuple) of the new position of the square
                defined by 2 positive integers
        Raises:
            TypeError: if size not an integer
            ValueError: if size less than 0
        Returns:
            the size of the square
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

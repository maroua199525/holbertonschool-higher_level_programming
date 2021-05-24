#!/usr/bin/python3
""" Module Rectangle"""


class Rectangle:
    """ a rectangle class that define a rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width function to retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ width function to set the value to the width

        Args:
        value: integer

        Raise:
        TypeError("width must be an integer")
        ValueError("message width must be >= 0")

        Return:
        the widith with his value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width value must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height function to retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height function to set the value to the height

        Args:
        value: integer

        Raise:
        TypeError("height must be an integer")
        ValueError(" height must be >= 0")

        Return:
        the widith with his value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height value must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ area function to calculate the area of the rectangle

        Return:
            the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):

        """ perimeter function to calculate the perimetr of the rectangle

        Return:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return(perimeter)

    def __str__(self):
        """
            print the rectangle
        Return:
            printed rectangle with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        new = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                new += symbol
            if i != (self.__height - 1):
                new += '\n'
        return new

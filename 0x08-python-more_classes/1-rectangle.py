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
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("message value must be >= 0")
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
        ValueError("message height must be >= 0")

        Return:
        the widith with his value
        """
        if type(value) is not int:
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("message value must be >= 0")
        else:
            self.__height = value

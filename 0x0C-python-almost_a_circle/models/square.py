#!/usr/bin/python3
""" Module contain one class: Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherit from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size function to retrievaluee the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """value function to set the value to the value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """ p"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **keywargs):
        """ update function that assigns attributes
        1st argument should be the id attribute
        2nd argument should be the value attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if args != ():
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in keywargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary
        representation of a square
        """
        dic = {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return dic

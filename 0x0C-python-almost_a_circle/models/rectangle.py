#!/usr/bin/python3
""" Module contain one class: Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """ Calling the super class with id -
        this super call with use the logic of the __init__ of the Base
        class """
        super().__init__(id)

    @property
    def width(self):
        """ width function to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ width function to retrieve the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height function to retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ height function to set the value to the height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x function to retrieve the x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ x function to set the value to the x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y function to retrieve the y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ y function to set the value to the y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
         that returns the area value of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """that prints in stdout the Rectangle instance with the character #
        """
        for x in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for j in range(0, self.__x):
                print(" ", end="")
            for k in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ print """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """ function that assigns a key/value argument to attributes:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if args != ():
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            returns the dictionary
            representation of a Rectangle
        """
        dictionary = {'x': self.__x, 'y': self.__y, 'id': self.id,
                      'height': self.__height, 'width': self.__width}
        return dictionary

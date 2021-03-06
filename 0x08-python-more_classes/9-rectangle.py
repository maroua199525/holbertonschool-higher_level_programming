#!/usr/bin/python3
""" Module Rectangle"""


class Rectangle:
    """ a rectangle class that define a rectangle"""

    # A class variable, counting the number of instances
    number_of_instances = 0
    # A class variable , printing the symbol #
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    # Decremented during each instance deletion
        Rectangle.number_of_instances += 1
        self.print_symbol

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
        the width with his value
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
        ValueError(height must be >= 0")

        Return:
        the height with his value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("hieght must be >= 0")
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

    def __repr__(self):
        """
        string representation of the rectangle
        Return:
            a string representation of the rectangl
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        delete function is the destructor

        """
        print("Bye rectangle...")
        # When new instance delated
        # subs to number of instances
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger_or_equal function that compare the area of two rectangle

        Args:
            rect_1: an instance of rectangle
            rect_1: an instance of rectangle

        Return:
            returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = Rectangle.area(rect_1)
        area2 = Rectangle.area(rect_2)
        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ return a new Rectangle instance with width == height == size
        Args:
        cls: class
        size: integer

        Return:
        a new Rectangle instance
        """

        return cls(size, size)

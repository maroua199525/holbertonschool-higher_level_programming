#!/usr/bin/python3
""" This module contains one class: Rectangle, that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ __init__ method """
    def __init__(self, width=0, height=0):
        """
        instantiation
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

#!/usr/bin/python3
# 0-rectangle.py
"""
This module defines a Rectangle Class
"""


class Rectangle():
    """
    Create a Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

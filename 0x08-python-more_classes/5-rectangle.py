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
        self.height = height
        self.width = width

    def __del__(self):
        """ Method that prints a message when the instance is deleted


        """
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
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

    def __str__(self):
        """ Method that returns the Rectangle #

        Returns:
            str of the rectangle


        """
        rectangle = ""
        if self.__width > 0:
            for y in range(self.__height):
                rectangle += ("#" * self.__width) + "\n"
        return rectangle[:-1]

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.__width, self.__height)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
                                            my_rectangle.perimeter()))

    del my_rectangle

    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

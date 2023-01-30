#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from
BaseGeometry (7-base_geometry.py)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that defines a base geometry
    """
    def __init__(self, width, height):
        super()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __repr__(self) -> str:
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self) -> str:
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())

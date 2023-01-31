#!/usr/bin/python3
"""
This module defines a class Square that inherits from
Rectangle (9-rectangle.py)
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

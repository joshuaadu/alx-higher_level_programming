#!/usr/bin/python3
class Square:
    """Defines a square with with a size attribute of type integer
    and is greater than 0"""
    def __init__(self, size=0) -> None:
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except Exception:
            raise

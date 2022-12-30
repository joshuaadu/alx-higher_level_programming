#!/usr/bin/python3
class Square:
    """Defines a square with with a size attribute of type integer
    and is greater than 0"""
    def __init__(self, size=0) -> None:
        """Initialize a new square"""
        self.__check_size(size)

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Get size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square"""
        self.__check_size(value)

    def __check_size(self, size):
        """Validate size input"""
        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except Exception:
            raise

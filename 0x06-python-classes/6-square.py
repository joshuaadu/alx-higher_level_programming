#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Defines a square with with a size attribute of type integer
    and is greater than 0"""
    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initialize a new square"""
        self.__validate_size(size)
        self.__validate_position(position)

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        # if size is equal to 0, print an empty line
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for i in range(self.__position[0])]
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Get size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square"""
        self.__validate_size(value)

    @property
    def position(self):
        """Get position of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set position of the square"""
        self.__validate_position(value)

    def __validate_size(self, size):
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

    def __validate_position(self, position):
        """Validate position input"""
        try:
            if type(position) is tuple and len(position) == 2 \
                    and type(position[0] == int) and type(position[1] == int):
                self.__position = position
            else:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
        except Exception:
            raise

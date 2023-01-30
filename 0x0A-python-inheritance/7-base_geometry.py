#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""


class BaseGeometry:
    """
    A class that defines a base geometry
    """

    def area(self):
        """Calculate area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        you can assume name is always a string

        if value is not an integer: raise a TypeError exception,
            with the message <name> must be an integer

        if value is less or equal to 0: raise a ValueError
            exception with the message <name> must be greater than 0

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

#!/usr/bin/python3
# 0-add_integer.py
"""
Defines an a function that performs integer additions
"""


def add_integer(a, b=98):
    """
        Adds 2 integers: a and b must be integers or floats

        Raise a TypeError exception with the message a must be
        an integer or b must be an integer

        a and b are first casted to integers if they are float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

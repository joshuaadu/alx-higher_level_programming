#!/usr/bin/python3
# 3-say_my_name.py

"""
This module defines a function that prints
the full name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    Returns the full name of a person
    My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")

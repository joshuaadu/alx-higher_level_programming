#!/usr/bin/python3
"""
This module defines a method that returns
the list of available attributes and methods of an object
"""


class Me:
    name = "me"


def lookup(obj):
    """
    returns the list of available attributes and methods of an object:
    """
    return dir(obj)


if __name__ == "__main__":
    me = Me()
    print(lookup(me))

#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


if __name__ == "__main__":
    print(MyClass("me").__dict__)

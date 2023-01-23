#!/usr/bin/python3
"""
This module defines an inherited list class MyList...
"""


class MyList(list):
    """Implements a sorted printing for the built-in list class"""
    def __init__(self):
        super()

    def print_sorted(self):
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)

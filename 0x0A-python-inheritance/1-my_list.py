#!/usr/bin/python3
"""
This module defines an inherited list class MyList...
"""


class MyList(list):
    """Implements a sorted printing for the built-in list class"""
    def print_sorted(self):
        print(sorted(self))

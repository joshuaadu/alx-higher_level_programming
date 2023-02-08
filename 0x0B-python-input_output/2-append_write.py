#!/usr/bin/python3
"""
This module defines a function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    appends a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        # pass
        return f.write(text)


if __name__ == "__main__":
    nb_characters = append_write("text.txt",
                                 "This School is so cool!\n")
    print(nb_characters)

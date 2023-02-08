#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "r+", encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    nb_characters = write_file("text.txt",
                               "This School is so cool!\n")
    print(nb_characters)

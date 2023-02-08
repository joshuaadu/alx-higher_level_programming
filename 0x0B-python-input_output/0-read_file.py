#!/usr/bin/python3
"""
This module defines a function that reads a file
"""


def read_file(filename=""):
    """
     reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)


def read_file_binary(filename=""):
    with open(filename, "rb") as f:
        read_data = f.read()
        print(read_data)


if __name__ == "__main__":
    read_file("text.txt")
    read_file_binary("text.txt")

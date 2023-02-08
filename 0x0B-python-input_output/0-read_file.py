#!/usr/bin/env python3
"""
This module defines a function that reads a file
"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read(2)
        print(read_data)
        print("tell:", f.tell())
        f.seek(1)
        print(f.read())


def read_file_binary(filename=""):
    with open(filename, "rb") as f:
        read_data = f.read()
        print(read_data)


if __name__ == "__main__":
    read_file("text.txt")
    read_file_binary("text.txt")

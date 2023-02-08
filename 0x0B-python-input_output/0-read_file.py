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
        print(read_data, end="")


def read_file_binary(filename=""):
    with open(filename, "rb") as f:
        # print(dir(f))
        read_data = f.read()
        print(read_data)
        print("tell:", f.tell())
        f.seek(0)

        """
        Using the format() string method, you can print out the line number
        and the line itself. The format specifier{:>4} means “print this
        argument right-justified within 4 spaces.” The a_line variable
        contains the complete line, carriage returns and all. The rstrip()
        string method removes the trailing whitespace, including the
        carriage return characters.
        """
        line_number = 0
        for line in f:
            line_number += 1
            print('{:>4} {}'.format(line_number, line.rstrip()))

        print(f.read())


if __name__ == "__main__":
    read_file("text.txt")
    read_file_binary("text.txt")

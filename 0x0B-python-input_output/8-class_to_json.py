#!/usr/bin/python3
"""
A module that defines a class to JSON function
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object
    """
    return obj.__dic__

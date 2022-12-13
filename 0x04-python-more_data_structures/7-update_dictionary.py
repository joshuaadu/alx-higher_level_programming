#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary"""
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary |= {key: value}
    # a_dictionary.update([(key, value)])
    return a_dictionary

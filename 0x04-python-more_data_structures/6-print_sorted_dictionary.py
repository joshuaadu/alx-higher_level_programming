#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    # get list of keys
    keys = list(a_dictionary)
    # sort keys
    keys.sort()
    # keys = sorted(a_dictionary)
    # loop through dict and print out each item
    for key in keys:
        print("{:s}: {:s}".format(key, str(a_dictionary[key])))

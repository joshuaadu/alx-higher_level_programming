#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list"""
    # loop through the list
    # find element to replace
    # replace with new element
    # return new list
    return list(map(lambda x: x if x != search else replace, my_list))
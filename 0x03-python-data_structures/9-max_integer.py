#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max_i = my_list[0]
    for x in my_list:
        if x > max_i:
            max_i = x
    return max_i

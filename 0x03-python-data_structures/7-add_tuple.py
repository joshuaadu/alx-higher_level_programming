#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a == 0:
            new_tuple_a = 0, 0,
        else:
            new_tuple_a = tuple_a[0], 0
    else:
        new_tuple_a = tuple_a
    if len_b < 2:
        if len_b == 0:
            new_tuple_b = 0, 0
        else:
            new_tuple_b = tuple_b[0], 0
    else:
        new_tuple_b = tuple_b
    return (new_tuple_a[0] + new_tuple_b[0], new_tuple_a[1] + new_tuple_b[1])

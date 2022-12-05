#!/usr/bin/python3
def no_c(my_string):
    return "".join([x for x in my_string if x != "c" and x != "C"])
# new_string = ""
# for x in my_string:
#   if x != "c" and x != "C":
#       new_string += x
# return new_string

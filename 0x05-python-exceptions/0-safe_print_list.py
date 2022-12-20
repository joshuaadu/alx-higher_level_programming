#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            num += 1
            print("{}".format(my_list[i]), end="")
        except Exception:
            break
    print("")
    return (num)

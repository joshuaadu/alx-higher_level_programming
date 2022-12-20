#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in range(x):
            num += 1
            print(my_list[i], end="")
    except Exception:
        raise
    finally:
        print("")
        return num

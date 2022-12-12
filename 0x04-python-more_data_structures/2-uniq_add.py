#!/ust/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)"""
    # find unique numbers
    uniq_list = set(my_list)
    # loop through unique numbers and add them
    sum = 0
    for num in uniq_list:
        sum += num
    return sum

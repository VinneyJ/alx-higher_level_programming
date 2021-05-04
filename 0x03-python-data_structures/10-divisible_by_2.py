#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return (None)
    new_list = my_list[:]
    for x in new_list:
        if not x % 2:
            new_list[x] = True
        else:
            new_list[x] = False
    return new_list

#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    moded_list_sum = 0
    for x in new_list:
        moded_list_sum += x
    return moded_list_sum

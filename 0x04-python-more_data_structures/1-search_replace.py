#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in new_list:
        if new_list.index(i) == search:
            new_list[search] = replace
    return new_list

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        for x in my_list:
            if idx == my_list.index(x):
                my_list[idx] = element
                return my_list

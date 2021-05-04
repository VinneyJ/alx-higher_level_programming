#!/usr/bin/python3
def no_c(my_string):
    letter = ""
    for x in range(0, len(my_string)):
        if my_string[x] != 'C' and my_string[x] != 'c':
            letter = letter + my_string[x]
    return letter

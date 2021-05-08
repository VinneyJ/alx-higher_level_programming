#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_key = sorted(a_dictionary.values())
        for k in a_dictionary:
            if a_dictionary[k] == max_key[-1]:
                return k
    else:
        return None

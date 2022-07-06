#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    first_item = list(a_dictionary)[0]
    largest = a_dictionary[first_item]
    largest_key = list(a_dictionary)[0]
    for k, v in a_dictionary.items():
        if v > largest:
            largest = v
            largest_key = k
    return largest_key

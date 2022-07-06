#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {}
    if key not in list(a_dictionary):
        a_dictionary[key] = value
    for k, v in a_dictionary.items():
        if k == key:
            new_dict[key] = value
        else:
            new_dict[k] = v
    return new_dict

#!/usr/bin/python3
"""write to json file"""


import json

def save_to_json_file(my_obj, filename):
    my_string_obj = str(my_obj)
    with json.dump(my_string_obj, filename) as j:
        j(my_string_obj, filename)




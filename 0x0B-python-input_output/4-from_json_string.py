#!/usr/bin/python3
"""Return Json format"""


import json


def from_json_string(my_str):
    """load json string in json format"""
    return json.loads(my_str)

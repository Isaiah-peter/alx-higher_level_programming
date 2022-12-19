#!/usr/bin/python3
"""check if class inherited from"""


def inherits_from(obj, a_class):
    """check if class inherited from"""
    return isinstance(obj, a_class) and type(obj) != a_class

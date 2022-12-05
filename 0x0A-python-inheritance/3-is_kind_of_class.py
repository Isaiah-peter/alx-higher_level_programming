#!/usr/bin/python3
"""check if class are kind of the same"""


def is_kind_of_class(obj, a_class):
    """check if class  kind of are the same"""
    if isinstance(obj, a_class):
        return True
    return False

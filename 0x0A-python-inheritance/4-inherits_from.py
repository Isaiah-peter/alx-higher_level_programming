#!/usr/bin/python3
"""check if class inherited from"""


def inherits_from(obj, a_class):
    """check if class inherited from"""
    return a_class.__init_subclass__ != obj.__init_subclass__
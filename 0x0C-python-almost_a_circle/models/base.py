#!/usr/bin/python3
"""create the base class"""


class Base:
    """
    base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

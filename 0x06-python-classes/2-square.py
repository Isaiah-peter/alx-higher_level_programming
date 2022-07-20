#!/usr/bin/python3
"""A Square Class with private attribute and validations"""


class Square:
    """A class that have a private attribute size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

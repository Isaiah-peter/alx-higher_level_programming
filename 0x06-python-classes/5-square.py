#!/usr/bin/python3
"""A Square Class with private attribute
 and validations and method with a setter"""


class Square:
    """A class that have a private attribute size and
    calculate the area and also change value with setter"""
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = size
        except ValueError:
            raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if value >= 0:
                self.__size = value
        except ValueError:
            raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for _ in range(0, self.__size):
                print("#", end="")
            print()

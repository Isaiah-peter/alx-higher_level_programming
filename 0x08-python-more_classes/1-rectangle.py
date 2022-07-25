#!/usr/bin/python3
"""A Rectangle Class"""


class Rectangle:
    """
    Rectangle class with instance method width
    and height and instance Attribute
    width and height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property

    def height(self):
        return self.__height

    @height.setter

    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property

    def width(self):
        return self.__width

    @width.setter

    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = width


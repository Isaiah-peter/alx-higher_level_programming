#!/usr/bin/python3
"""create Rectangle class and inherit
from base geometry
"""


class Rectangle(BaseGeometry):
    """create Rectangle class and inherit
    from base geometry
    """
    def __init__(self, width, height):
        """create Rectangle class and inherit"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = self
        self.__height = height

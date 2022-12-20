#!/usr/bin/python3
"""create Rectangle class and inheritfrom base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create Rectangle class and inherit
    from base geometry
    """
    def __init__(self, width, height):
        """create Rectangle class and inherit"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return string representation of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """calculate area of rectangle"""
        return self.__height * self.__width

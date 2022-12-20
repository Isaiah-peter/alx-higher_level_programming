#!/usr/bin/python3
"""Create Square Class that inherit from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Create a Square class that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """return string representation of rectangle"""
        return f"[Rectangle] {self.__size}/{self.__size}"

    def area(self):
        """calculate area of rectangle"""
        return self.__size * self.__size
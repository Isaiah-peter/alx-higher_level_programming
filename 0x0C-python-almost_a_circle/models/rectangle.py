#!/usr/bin/python3
"""create rectangle class"""


from models.base import Base


class Rectangle(Base):
    """create Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """properties of class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
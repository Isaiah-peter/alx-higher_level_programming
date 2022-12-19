#!/usr/bin/python3
"""create Rectangle class and inherit
from base geometry
"""

#!/usr/bin/python3
"""create a new Class called BaseGeometry"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))



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

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
        if self.__size is 0:
            print()
        for i in range(0, self.__size):
            for _ in range(0, self.__size):
                print("#", end="")
            print()
            
    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square in 2D space
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

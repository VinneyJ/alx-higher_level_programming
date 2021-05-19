#!/usr/bin/python3
"""Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            "size must be an integer, otherwise raise a TypeError"
            raise TypeError("size must be an integer")
        elif value < 0:
            "size must be more than zero"
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)

#!/usr/bin/python3
class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        if type(size) is not int:
            "size must be an integer, otherwise raise a TypeError"
            raise TypeError("size must be an integer")
        elif size < 0:
            "size must be more than zero"
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

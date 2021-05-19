#!/usr/bin/python3
class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            "size must be an integer, otherwise raise a TypeError"
            raise TypeError("size must be an integer")
        if size < 0:
            "size must be more than zero"
            raise ValueError("size must be >= 0")
        self.__size = size

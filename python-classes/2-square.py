#!/usr/bin/python3
"""
this module defines a class Square with input validation and area calculation.
it demonstrates the use of public methods to expose private data behavior.
"""


class Square:
    """
    it represents a square with strict size validation.

    attributes:
        __size (int): the size of the square (private).
    """
    def __init__(self, size=0):
        """
        initialise the square with type and value checks.

        args:
            size (int): the size of the square.defaults to 0.

        raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates and returns the area of the square.

        returns:
            int: the area of the square (size + size).
        """
        return self.__size ** 2

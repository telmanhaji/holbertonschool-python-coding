#!/usr/bin/python3
"""
this module defines a class Square with getters and setters.
it demonstrates centralized data validation using python properties.
"""


class Square:
    """
    it represents a square with strict size validation.

    attributes:
        __size (int): the size of the square (private).
    """
    def __init__(self, size=0):
        """
        initializes the square using the setter.

        args:
            size (int): the size of the square. defaults to 0.
        """
        # key change: it assigns to 'self.size', not 'self.__size'.
        # this ensures the validation logic in the setter runs immediately
        # when the object is created
        self.__size = size

    @property
    def size(self):
        """
        retrieves the size of the square.

        returns:
            int: the current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square with validation.

        args:
            value (int): the new size

        raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        # 1st. type validation
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # 2nd. value validation
        if value < 0:
            raise ValueError("size must be >= 0")

        # 3rd. secure update
        self.__size = value

    def area(self):
        """
        calculates and returns the area of the square.

        returns:
            int: the area of the square.
        """
        return self.__size ** 2

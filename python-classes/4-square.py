#!/usr/bin/python3
"""
defines a class Square with validation, area calculation, and printing.
it demonstrates how to visualize object state.
"""


class Square:
    """
    represents a square with strict size validation.

    attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        initializes the square using the setter.

        args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        retrieves the size of the square.

        returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square with validation.

        args:
            value (int): The new size.

        raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates and returns the area of the square.

        returns:
            int: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square with the character #.
        if size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # loop for rows
        for i in range(self.__size):
            # loop for columns (or just print the string multiplied)
            # in python, "#" * 3 results in "###"
            print("#" * self.__size)

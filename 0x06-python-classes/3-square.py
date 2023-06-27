#!/usr/bin/python3

class Square:
    """This represent a square."""

    def __init__(self, size=0):
        """This initialize a new square.
        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This returns current area of the square."""
        return (self.__size * self.__size)

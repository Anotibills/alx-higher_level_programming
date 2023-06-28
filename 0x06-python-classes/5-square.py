#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """This is used to represent a square."""

    def __init__(self, size):
        """This initializes a new square.
        Args:
            size (int): This is the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """This get/set the current size of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This returns the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """This prints the square with the # character."""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")


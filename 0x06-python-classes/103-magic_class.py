#!/usr/bin/python3
import math
class MagicClass:
    """This represent a circle."""

    def __init__(self, radius=0):
        """this initializes a MagicClass.
        Arg:
            radius (float or int): This is the radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This will return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """This will return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)


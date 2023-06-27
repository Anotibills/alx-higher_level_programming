#!/usr/bin/python3

class Square:
    """This is used to represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """This initializes a new square.
        Args:
            size (int): This is the size of the new square.
            position (int, int): This is the position of the new square.
        """
        self.size = size
        self.position = position

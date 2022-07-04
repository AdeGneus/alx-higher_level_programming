#!/usr/bin/python3

"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """Represent a Square inherited from Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.
        Args:
            size (int): size of the Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, self)
        self.__size = size

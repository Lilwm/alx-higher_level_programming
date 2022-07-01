#!/usr/bin/python3
"""
class Square that defines a square
size must be an integer else raise a value error
if size < 0 raise value error
"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) **2

#!/usr/bin/python3
"""
class Square that defines a square
"""
class Square:
    """
    represents a class square
    Attributes:
        __size(int): size of a side of the square
    """
    def __init__(self, size=0):
        """initialize a square
        Args:
            size(int) : size of the side of a square
        Returns: None
        """
        self.__size = size
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

#!/usr/bin/python3
""" a class with width and height properties """


class Rectangle:
    """initiate the class"""
    def __init__(self, width=0, height=0):
        """set private instance width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter of __width
        Returns: width(int)"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter of __width Value(int) size of width
        raise typeerror not int  or value error if < 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of height
        Returns: height(int)"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height Value(int) size of width
        raise typeerror not int  or value error if < 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

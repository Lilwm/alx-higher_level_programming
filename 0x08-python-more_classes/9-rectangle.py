#!/usr/bin/python3
""" a class with width and height properties """


class Rectangle:
    """ Class attribute"""
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance that is square"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method to return biggest rectangle based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """set private instance width and height"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter of __width
        Returns: width(int)"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width Value(int) size of width
        raise typeerror not int  or value error if < 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """public instance method that defines the area"""
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """returns a printable representation of the rectangle"""
        string = ""
        if self.width != 0 and self.height != 0:
            string += "\n".join(str(self.print_symbol) * self.width for j in range(self.height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

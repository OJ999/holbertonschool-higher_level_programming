#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square"""

    def __init__(self, size):
        """Initializes a square with a given size"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Computes the area of the square"""
        return self.__size * self.__size


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())

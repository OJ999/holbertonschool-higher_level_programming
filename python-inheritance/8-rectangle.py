#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle with a given width and height"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

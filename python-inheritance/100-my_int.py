#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """A class representing a rebel integer"""

    def __eq__(self, other):
        """Overrides the equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality operator"""
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)

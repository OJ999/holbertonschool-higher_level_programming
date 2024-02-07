#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from the specified class"""
    return isinstance(obj, a_class) and type(obj) != a_class


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))

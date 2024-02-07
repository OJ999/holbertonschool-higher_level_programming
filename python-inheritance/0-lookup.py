#!/usr/bin/python3
"""
This module contains a function to return the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be looked up.

    Returns:
        A list object containing the attributes and methods of the object.
    """
    return dir(obj)

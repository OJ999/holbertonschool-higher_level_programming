#!/usr/bin/python3
"""
Module to convert an object to a JSON serializable dictionary
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: An instance of a Class with serializable attributes

    Returns:
        dict: Dictionary representation of the object
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Filter out private and callable attributes
    serializable_attributes = {key: value for key, value in attributes.items()
                               if not (key.startswith('__') and key.endswith('__'))
                               and not callable(value)}

    return serializable_attributes

if __name__ == "__main__":
    pass  # This module is meant to be imported and used elsewhere

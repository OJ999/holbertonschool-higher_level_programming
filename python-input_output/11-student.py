#!/usr/bin/python3
"""
Module to define a Student class
"""

class Student:
    """
    A class to represent a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list of str, optional): List of attribute names to retrieve.

        Returns:
            dict: A dictionary containing the specified attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
    pass  # This module is meant to be imported and used elsewhere

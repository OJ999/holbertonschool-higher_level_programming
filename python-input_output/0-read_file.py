#!/usr/bin/python3
"""Module to read a text file and print its content to stdout."""


def read_file(filename=""):
    """Read a text file and print its content to stdout.

    Args:
        filename (str): The name of the file to read.

    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')

if __name__ == "__main__":
    read_file()

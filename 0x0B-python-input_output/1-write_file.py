#!/usr/bin/python3
"""Define file-writing function."""


def write_file(filename="", text=""):
    """
    read file by utf-8

    Args:
        filename: The name of the file to write
        text: The text to write to the file.
    Returns:
        The number of characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

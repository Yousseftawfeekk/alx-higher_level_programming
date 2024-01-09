#!/usr/bin/python3
"""Define file-appending function"""


def append_write(filename="", text=""):
    """
    Append a string to the end of UTF8 text file

    Args:
        filename: The name of the file to append to.
        text: The string to append to the file.
    Returns:
        The number of char appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

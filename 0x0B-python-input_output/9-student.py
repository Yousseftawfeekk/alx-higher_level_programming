#!/usr/bin/python3
"""Define class student."""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """Initialize new student.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary of the Student."""
        return self.__dict__

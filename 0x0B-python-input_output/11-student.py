#!/usr/bin/python3
"""Define class student"""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize new Student

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student

        Args:
            attrs: The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(att) == str for att in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student.

        Args:
            json: The key and value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)

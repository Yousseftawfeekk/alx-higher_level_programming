#!/usr/bin/python3
"""Define class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionar of simple data structure."""
    return obj.__dict__

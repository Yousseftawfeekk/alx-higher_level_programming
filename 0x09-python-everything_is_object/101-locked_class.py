#!/usr/bin/python3
"""Defining locked class"""


class LockedClass:
    """
    prevent the user from instantiating new lockedclass attributes
    for anything but attribute called 'first_name'

    """

    __slots__ = ["first_name"]

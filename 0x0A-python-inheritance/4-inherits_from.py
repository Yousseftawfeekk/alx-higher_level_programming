#!/usr/bin/python3
'''module for inherits_from method'''


def inherits_from(obj, a_class):
    '''determines if object is true subclass of a clas'''
    return isinstance(obj, a_class) and type(obj) != a_class

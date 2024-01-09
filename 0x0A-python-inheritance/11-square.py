#!/usr/bin/python3
'''module for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' subclass representing a rectangle.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method area of square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns string rep this square'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)

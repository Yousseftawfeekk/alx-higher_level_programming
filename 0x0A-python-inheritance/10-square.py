#!/usr/bin/python3
'''Module Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''subclass representing a rectangle.'''
    def __init__(self, size):
        '''constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method area of square.'''
        return self.__size ** 2

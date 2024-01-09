#!/usr/bin/python3
'''Contains class MyInt'''


class MyInt(int):
	'''rebel version of an integer, perfect for opposite day!'''
    def __new__(cls, *args, **kwargs):
        '''create instance of the class'''
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        '''what was not eq is now eq'''
        return int(self) != other

    def __ne__(self, other):
        '''what was eq is now not eq'''
        return int(self) == other

#!/usr/bin/python3
''' module to sort mylist'''

class MyList(list):
    ''' my list class '''

    def print_sorted(self):
        ''' method for printing sorted list'''
        print(sorted(self))


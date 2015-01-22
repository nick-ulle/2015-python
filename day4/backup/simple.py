'''
Write what your program does here in the header
'''

# Imports come first
import json


print('This runs when the script is imported')


def greet(person):
    '''
    This is a function docstring
    '''
    print('hello', person)


if __name__ == '__main__':

    # Put the action code here
    # Also a good place for tests

    print('the __name__ is __main__!')
    greet('Matt')

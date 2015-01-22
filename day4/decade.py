'''
Tools for working with dates
'''

#import pandas as pd

def decade(year):
    '''
    Given a year, return the decade

    >>> decade(1986)
    1980

    '''
    return 10 * (year // 10)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

'''
Lecture 4

Wed Jan 21 20:41:05 PST 2015

Today's Goals:
    - functions
    - scripting
    - pandas

A python script is just a plain text file with a .py extension. It contains
a bunch of commands which will be executed in the order that they appear.

Pandas gives us the DataFrame and all the power that comes with it.

Data Munging: Putting your data into the correct form and type for
analysis. This is the foundation for any analysis you wish to do. It pays
to be able to do it efficiently.

Glamour: *
Utility: *****

Pandas makes data munging easier.

Documentation and doctests are sooooo easy in Python. 
'''

def decade(year):
    '''
    Return the decade of a given year

    >>> decade(1954)
    1950

    '''
    return 10 * (year // 10)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

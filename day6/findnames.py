'''
We'd like to pick the names out of text.

Our simple approach:

A regular expression for words beginning with an uppercase letter
which are not at the beginning of a sentence

points: 
- r for \n
'''

import re

pattern = re.compile(r'''
        [^^]            # Not the beginning of a string
        (?<!\.\s)       # No period in front
        [A-Z]           # single uppercase letter
        [a-z]{1,}       # at least 1 lowercase letter
''', flags=re.VERBOSE)

pattern2 = re.compile(r'[^^](?<!\.\s)[A-Z][a-z]{1,}')


s = 'Hello there Yeji. Your baby will be named Joe.'

g = pattern.findall(s)

print(g)

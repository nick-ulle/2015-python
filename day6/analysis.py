'''
We'd like to do network analysis on a body of text.

Build a graph where the nodes are names, and an edge exists if the two
names appear in the same sentence.

The first rule about regular expressions:
    Avoid them when possible!!!!

Data Golf!
Today it's for a prize- a book on Python
Hints:
    - An ASCII character of text is 1 byte
    - A typical word is 6 characters
    - A typical novel has 200K words
    - War and Peace is 3x a normal book

How big is War and Peace?

regex should match capital letters not at the beginning of a sentence.
'''

import re
from itertools import combinations
import networkx as nx

names = 'Nick Clark Rick Qi'.split(' ')

namepairs = set(combinations(names, 2))

pattern = re.compile(r'''
        [^^]        # Not the beginning of a string
        (?<!\.\s)   # Exclude the period
        [A-Z]       # A single capital letter
        [a-z]{1,}   # Rest of the word
''', flags=re.VERBOSE)

pattern2 = re.compile(r'[^^](?<!\.\s)[A-Z][a-z]{1,}')


s = '''The teachers are Nick and Clark.
The students include Rick and Qi.
'''

print(pattern.findall(s))

sentences = s.split('.')

def together(namepair, sentence):
    '''
    Return True if all the elements of namepair are in
    the sentence
    '''
    return all(x in sentence for x in namepair)


G = nx.Graph()

for s in sentences:
    for namepair in namepairs:
        if together(namepair, s):
            # * does unpacking
            G.add_edge(*namepair)


















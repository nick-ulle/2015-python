'''
A data driven approach to naming babies

Names and counts are from the US Social Security office for 2013.
3.6 million - probably all the babies born in 2013
'''

import numpy as np
import pandas as pd

names = pd.read_csv('yob2013.txt', names=['name', 'gender', 'count'])

# Assign probabilities
names['probs'] = names['count'] / names['count'].sum()


def babynamer():
    '''
    Returns a baby name and gender
    '''
    i = np.random.choice(len(names), p=names['probs'])
    return  names.iloc[i, :]



if __name__ == '__main__':

    b1 = babynamer()

    s = '''
    {} is a {}. In 2013 there were {:,} babies with that name. The
    probability is {:.3g}.
    '''

    sfull = s.format(*b1)

    print(sfull)


    s2 = '''
    {name} is a {gender}. In 2013 there were {count:,} babies with that name. 
    The probability is {probs:.3g}.
    '''

    s2full = s2.format(**b1)

    print(s2full)

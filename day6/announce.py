'''
A data driven approach to naming babies
'''

import numpy as np

from babynamer import babynamer

# Set a random seed to get the same name
np.random.seed(812)

b = dict(babynamer())

# This part is called the template

dearwife = '''
Yeji is having a baby {gender}.
The name will be {name}. In 2013,
there were {count:,} babies with this name. 
The probability of getting this name was {probs:.3g}.
'''

print(dearwife.format(**b))

with open('dearyeji.txt', 'w') as f:
    f.write(dearwife.format(**b))

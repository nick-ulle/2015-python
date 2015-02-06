'''
Fitting a beta distribution to the sleep data
'''

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

sleep = pd.read_csv('sleepminutes.csv')
sleep = sleep['minutes'] / 60

# Fit the MLE of the beta distribution
p = stats.beta.fit(sleep, floc=0, fscale=24)

# The corresponding random variable
Xsleep = stats.beta(*p)

plt.hist(sleep, bins=30, normed=True)
x = np.linspace(0, 24)
plt.plot(x, Xsleep.pdf(x), linewidth=4)
s = 'alpha: {:.3}, beta: {:.3}, loc: {}, scale: {}'
plt.title(s.format(*p))
plt.savefig('sleep.pdf')

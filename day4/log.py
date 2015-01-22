# first lets look at what we have
dir()
# lets pull in everything from Numpy
from numpy import *
dir()
%pylab
plot?
# everything in matplotlib and numpy have become global variables
# This is recommended interactive work- but not for scripting or programming
import seaborn
# Seaborn gives pretty graphics
plot([0, 1, 0])
# In summary just use %pylab
import pandas as pd
import pandas as penguins
# I could have given pandas any name I want
import numpy as np
# Pandas maintains data integrity across operations
a = pd.Series(np.ones(10))
a
a
type(a)
# the dataframe is like a table
# the columns in a dataframe are called series
a
b = pd.Series(np.ones(5))
b
type(b)
b
b.index
a + b
pd.date_range('2014-01-01', periods=10)
a
pd.date_range('2014-01-01', periods=10)
a.index
a.index[1]
a.index[1] = 29
a.index = pd.date_range('2014-01-01', periods=10)
a
a.index = pd.date_range('2014-01-01', periods=10)
b.index = pd.date_range('2014-01-03', periods=5)
a
b
a + b
a
a[:10]
a[4]
# Now for real data
# Pandas makes it very easy to read and write data
# in various formats
p = pd.read_csv('population.csv')
type(p)
# How big is it?
p.shape
# We have 186 rows
# and 3 columns
p.dtypes
p.head()
p.dtypes
p['Date'].head()
p['Date'][0]
d1 = p['Date'][0]
type(d1)
# Lets convert to datetime
pd.to_datetime(d1['Date'])
pd.to_datetime(p['Date'])
p['Date'] = pd.to_datetime(p['Date'])
p.dtypes
# How many countries are there?
p['ISO']
p['ISO'].unique()
p['ISO'].head()
p.head()
p.dtypes
p.pivot?
p2 = p.pivot(index='Date', columns='ISO', values='population')
p2.head()
# Now we can plot
p2.plot()
# I have another table
lang = pd.read_csv('languages.csv')
lang
p.head()
lang
wiki = pd.read_html('http://en.wikipedia.org/wiki/ISO_3166-1')
type(wiki)
len(wiki)
wiki[0]
w = wiki[0]
w.head()
w2 = w.iloc[1:, [0, 2]]
w2.head()
w2.columns
p.columns
lang.columns
w2.columns = ['country', ISO']
w2.columns = ['country', 'ISO']
w2.head()
lang.merge(w2)
p.head()
p.merge(lang.merge(w2))
p2 = p.merge(lang.merge(w2))
p2.columns
p2.head()
# given a year- how do we get the decade?
% run decade.py
# 1958 -> 1950
1958 // 10
10 * (1958 // 10)
%run decade.py
decade?
import decade
p2.dtypes
p2['year'] = p2.index.year
p2.index[:10]
p2.head()
p2.index = p2['Date']
p2.index.year
p2['year'] = p2.index.year
p2.dtypes
p2.head()
p2['year'].apply(decade)
p2['year'].apply(decade.decade)
p2['decade'] = p2['year'].apply(decade.decade)
p2.head()
# The question was- what was the mean population in China by decade?
p2.groupby(['country', 'decade'])
p2.groupby(['country', 'decade']).mean()
p3 = p2.groupby(['country', 'decade']).mean()
p3
pd.__version__
%history -f 'day4log.py'

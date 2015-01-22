clear
# The first thing we do is import the libraries we need
# This can get a little tiresome
# If I want to use everything in the Numpy library:
# First let's see what I have in base Python:
dir()
# Very little
# Suppose I now want everything from the Numpy library for my interactive work:
from numpy import *
dir()
# We just brought everything from Numpy into the workspace
# More precisely- they are all global variables and functions now
# This is convenient for interactive work
# But not recommended for scripting / programming
# Ipython makes this easy:
%pylab
# This imported everything from numpy and matplotlib and set up the plotting
import seaborn
# seaborn gives you pretty graphics :)
plot([1, 2, 1, 2])
import pandas as pd
import pandas as funstuff
clear
# Functions are a _wonderful_ thing
def greeter(name):
    print('hello', name)
greeter('Qi')
ls
%run country.py
# read in the population data
p = pd.read_csv('population.csv')
type(p)
p.shape
p.dtypes
# Date should be a timestamp, not object
# We need to fix it!
pd.to_datetime?
p
p.columns
# Lets start out with the basics
# Columns of a DataFrame are called Series
# The name comes from time series
# hint- they work really well for time series
pd.DateOffset?
pd.date_range?
a = pd.date_range('2014-01-01')
# I've just illustrated a valuable technique-
If you don't know what will happen, just try it and see what error you get
# If you don't know what will happen, just try it and see what error you get
a = pd.date_range('2014-01-01', periods=10)
a
aser = pd.Series(a)
aser
import numpy as np
a = np.ones(5)
a
aser = pd.Series(a)
aser
aser.index
# Pandas is designed to preserve the structure of your data
# That means the index will be maintained throughout the operations
bser = pd.Series(np.ones(10))
bser
aser
bser
aser + bser
# Alignment was preserved
aser
aser.index[0]
# This would be a crazy thing to doaser.index[0] = 27
aser.index[0] = 27
aser.index
a = aser
a
a.index
# Index is an attribut of a dataframe or series
a.index = pd.date_range('2014-01-01', periods=5)
a
b = bser
b.index = pd.date_range('2014-01-03', periods=10)
b
a
b
# Dataframes try hard to preserve alignment
a + b
a.data
a.as_matrix()
# Indexing is important
# You get speed and data integrity
p
p.dtypes
p.columns
# Selecting columns is like key lookups in a dictionary
p['Date']
p['Date'][:10]
p['Date'].head()
pd.to_datetime(p['Date'])
# Before we had strings
# These are nanosecond timestamps
p['Date'] = pd.to_datetime(p['Date'])
# I just updated my script with the new commands
# lets make sure it worked
%run country.py
p.dtypes
# type is correct
# We have another table:
c = pd.read_csv('languages.csv')
c
c.shape
c.dtypes
# Our goal is to put the language into the population table
p.head()
# But we don't have country names
wiki = pd.read_html('http://en.wikipedia.org/wiki/ISO_3166-1')
# You may expect this to be a DataFrame
# But HTML pages can contain many tables
type(wiki)
len(wiki)
wiki[0]
wiki[0].head()
# We only need columns 0 and 2
w = wiki[0].iloc[:, [0, 2]]
# df.iloc lets us do integer selction of rows, columns
w.shape
w.dtypes
w.head()
w.columns
w.columns = ['country', 'ISO']
w.columns
# Now for the join
l
dir()
sh short name (upper/lower case)  Alpha-3 code5
c
l = c
l
l
w
w.head()
w.columns
l.columns
l.merge(w)
p.columns
p2 = p.merge(l.merge(w))
p2.columns
p2.dtypes
p2.head()
# A successful join
p.head()
p['ISO'].unique()
p.shape
p.head()
p.pivot?
p.pivot(index='Date', columns='ISO', values='population')
p3 = p.pivot(index='Date', columns='ISO', values='population')
p3.dtypes
p3.head()
p3.iloc[:10, ]
p3.iloc[10:20, ]
p3
p3.plot()
p3.dtypes
p2
p2.head()
p2['language'].unique()
ppop = p2['population']
p2.groupby?
p2.groupby('language')
grouper = p2.groupby('language')
type(grouper)
grouper.name
grouper.ngroups
grouper.mean()
# Let's put this together
p2.groupby('language').mean()
p2.groupby('language').count()
grouper.mad?
grouper.size?
grouper.size()
# Suppose we want to know the average population in each country by decade
p
p2
p3
# Suppose we want to know the average population in each country by decade
# If p3 had a column with the decades we could do a groupby
p3.index
p3.index.year
p3
p3['year'] = p3.index.year
p3.dtypes
p3.head()
# We need to get the decade from the year
# ie 1954 -> 1950
1954 // 10
# floor division by 10
10 * 1954 // 10
10 * (1954 // 10)
%run country.py
%run country.py
%run country.py
decade
?decade
decade(2018)
p2
p3.dtypes
p3['year'].apply(decade)
p3['decade'] = p3['year'].apply(decade)
p3.head()
p3.groupby('decade').mean()
# So what if I want a column with this?
g = p3['CHN'].groupby('decade')
g = p3[['CHN', 'decade']].groupby('decade')
g.transform?
g.transform(np.mean)
p3['china10yr'] = p3[['CHN', 'decade']].groupby('decade').transform(np.mean)
p3.plot()
p3[['CHN', 'china10yr']].plot()
a = np.arange(20)
a
a // 10
ls
a = pd.read_html('ISO_3166-1')

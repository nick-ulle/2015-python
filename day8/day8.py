from scipy import stats
# Random variables
# Statistically: Z ~ N(0, 1)
Z = stats.norm(0, 1)
Z.mean()
Z.interval(0.95)
Z.ppf(0.975)
Z.std()
Z.pdf(0)
import matplotlib.pyplot as plt
plt.ion()
# plot density of normal from -4 to 4
import numpy as np
x = np.linspace(-4, 4)
Z
Z.pdf(x)
plt.plot(x, Z.pdf(x))
plt.plot(x, Z.cdf(x))
Z.sf?
plt.plot(x, Z.sf(x))
import pandas as pd
sleep = pd.read_csv('sleepminutes.csv')
sleep.shape
sleep.head()
sleep = sleep['minutes']
type(sleep)
# Lets model this with a statistical distribution
plt.hist(sleep)
sleep.min()
sleep.max()
24 * 60
# Goal- fit the MLE of the beta distribution
# to our sleep data
stats.beta.fit(sleep, floc=0, fscale=24*60)
Xsleep = stats.beta(stats.beta.fit(sleep, floc=0, fscale=24*60))
Xsleep = stats.beta(*stats.beta.fit(sleep, floc=0, fscale=24*60))
Xsleep
stats.beta.fit(sleep, floc=0, fscale=24*60))
stats.beta.fit(sleep, floc=0, fscale=24*60))
Xsleep
stats.beta?
sleep.mean()
Xsleep.mean()
# Now lets plot it
# Now lets plot it
h, edges = np.histogram(sleep, 30, normed=True)
h
plt.bar(edges[:-1], h, width=np.diff(edges))
plt.clf()
plt.bar(edges[:-1], h, width=np.diff(edges))
# Now add our fitted beta distribution
x = np.linspace(0, 60*24)
x
x = np.linspace(0, 60*24)
plt.plot(x, Xsleep.pdf(x), linewidth=4, color='orange')
# Now let's move on to the machine learning
clear
%run kaggle.py
type(titanic)
titanic.dtypes()
titanic.dtypes
clear
titanic.dtypes
clear
%run kaggle.py
X.shape
pd.factorize?
clear
titanic.dtypes
%run kaggle.py
clear
genders
a, b = (0, 1)
a
b
a, b = 0, 1
a
b
clear
%run kaggle.py
plt.hist?
clear
X.isnull().sum()
# Pull out stats module from Scipy
from scipy import stats
%run kaggle.py
X.shape
clear
rfmod
rfmod
rfmod.score()
# We're going to do cross validation
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(rfmod, X, y, cv=10)
scores
plt.box(scores)
q
plt.clf()
plt.box(scores)
plt.boxplot(scores)
scores
plt.boxplot(scores)
rfmod.predict(X)
rfmod.predict_proba(X)
a = rfmod.predict_proba(X)
a.shape
len(a)
a.size
%history -f day8.py

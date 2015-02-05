from scipy import stats
# stats is a scipy submodule, not an object

import matplotlib.pyplot as plt

plt.ion()
# Starting out:
# Statistically you might say Z ~ N(0, 1)
# To denote a normal random variable
Z = stats.norm(0, 1)
# This is how you do it in Python
# There is a tight correspondence between the code and the mathematical notation
# :)
# Both Python and Julia have had the luxury of learning from R
# I find random variables much more intuitive here
# For example:
# What's the mean?
Z.mean()
Z.median()
Z.interval(0.95)
# A 95 percent confidence interval
# The object oriented approach is quite convenient
Z.cdf(2)
Z.moment?
Z.moment(0)
Z.moment(1)
Z.moment(2)
Z.moment(3)
Z.pdf(0)
Z.ppf(0.975)
# percentage point function- also called quantile
# pmf is probability mass function- but continuous RV's don't have a pmf
Z.pmf(0)
Z.rvs(10)
Z.stats()
Z.std()
# scipy.stats supports nearly 100 different distributions
# And the all behave EXACTLY like this :)
stats.zipf?
Z2 = stats.zipf(4)
Z2.mean()
x = np.linspace(-2, 2)
# Visualize it
plt.plot(x, Z.pdf(x))
plt.clf()
plt.plot(x, Z.pdf(x))
x = np.linspace(-4, 4)
plt.plot(x, Z.pdf(x))
plt.plot(x, Z.cdf(x))
# You might ask- what's the survival function?
plt.plot(x, Z.sf(x))


# Now lets look at the sleep data that Nick introduced last time
# Some exploratory analysis of this distribution
# We'd like to see if we can fit a statistical distribution to this data.

import pandas as pd
sleep = pd.read_csv('sleepminutes.csv')
sleep.head()
type(sleep)
sleep = sleep['minutes']
# We're just working with one series here
plt.hist(sleep, bins=30)
# Suppose that we want to model this with an appropriate statistical distribution
# The only possible range of values are between 0 and 24 * 60
24 * 60
sleep.max()
# So somebody slept 23.5 / 24 hours
# It's possible to fit this using a beta distribution
# Beta is only defined on [0, 1]
sleep.min()
# So we'll need to scale it
# All RV's in Scipy have parameters for shape, location and scale
stats.beta.fit?
stats.beta.fit(sleep, floc=0, fscale = 24 * 60)
# floc means 'fixed location'
bparams = stats.beta.fit(sleep, floc=0, fscale = 24 * 60)
# We know the shape and scale, so we'll fit using this knowledge
# This is the MLE for alpha and beta parameters
# Now we make a random variable
sbeta = stats.beta(*bparams)
sbeta
sbeta.interval(1)
sbeta.mean()
sleep.mean()

# So sbeta here is the beta distribution fitted to this data
# Let's plot it and make sure
# that it looks reasonable

x = np.linspace(0, 60*24)
h, edges = np.histogram(sleep, 30, normed=True)
plt.bar(edges[:-1], h, width=np.diff(edges))
plt.plot(x, sbeta.pdf(x), linewidth=4, color='orange')

plt.clf()

# Titanic model building
preds = rfmod.predict(X)

plt.boxplot(scores)

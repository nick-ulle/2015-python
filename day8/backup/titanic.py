'''
Predict survivors of the Titanic
'''

import pandas as pd
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier


##################################################
# 
# 1) Prepare the data
#
# Machine learning is regression with a sexier name.
#
# Fitting regression models requires clean numeric data.
# Typically we have an n x 1 vector response y and an n x p 
# predictor matrix X. 
#
# Much of the art is in preparing an appropriate X. 
# Tasks include:
#   - Separating validation data set
#   - Joins / calculated columns
#   - transform categorical data and text
#   - impute missing data
# 
##################################################

# Read in the data
titanic = pd.read_csv('titanic.csv')

y = titanic['Survived']

# Some numeric features
features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

X = titanic[features].copy()

# Add in the gender
X['Sex'], genders = pd.factorize(titanic['Sex'])

# Need full rows
#X.fillna(X.mean(), inplace=True)
# Drop rows with missing data - although we could impute
fullrows = -X.isnull().any(axis=1)
X = X[fullrows]
y = y[fullrows]

##################################################
# 
# 2) Fit and evaluate models
# 
# Fitting models is easy in scikit learn.
#
# Some techniques:
#   - Cross validation
#   - Grid searches over model parameter spaces
#   - Various ways to score
# 
##################################################

rfmod = RandomForestClassifier()
rfmod.fit(X, y)

# How well did it perform?
# 10 fold cross validation
scores = cross_val_score(rfmod, X, y, cv=10)

##################################################
#
# 3) Predict
#
# Make predictions on new data using fitted model
#
##################################################

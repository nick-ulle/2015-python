'''
Titanic data set

Predict who will survive
'''

import pandas as pd

##################################################
# 
# 1) Prepare the data
#
# Machine learning - better marketing
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

titanic = pd.read_csv('titanic.csv')

y = titanic['Survived']

# Features to include in the model
features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

X = titanic[features].copy()

# Add in the gender
X['Sex'], genders = pd.factorize(titanic['Sex'])

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

from sklearn.ensemble import RandomForestClassifier

rfmod = RandomForestClassifier()

rfmod.fit(X, y)

##################################################
#
# 3) Predict
#
# Make predictions on new data using fitted model
#
##################################################

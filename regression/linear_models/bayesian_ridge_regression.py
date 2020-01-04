from sklearn import linear_model
import numpy as np

# data for fit
X = [[0.0,0.0],[1.0,1.0],[2.0,2.0],[3.0,3.0]]
y = [0.0,1.0,2.0,3.0]

# fit by Bayesian Ridge Regression
model = linear_model.BayesianRidge()
model.fit(X,y)

# print result(coefficient/intercept)
print(model.coef_)
print(model.intercept_)

# estimate
print(model.predict([[1.0,0.0]]))

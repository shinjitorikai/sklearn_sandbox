from sklearn import linear_model
import numpy as np

# data for fit
X = [[0,0],[1,1]]
y = [0,1]

# fit by Lasso Regression
model = linear_model.Lasso(alpha=0.1)
model.fit(X,y)

# print result(coefficient/intercept)
print(model.coef_)
print(model.intercept_)

# estimate
print(model.predict([[1,1]]))

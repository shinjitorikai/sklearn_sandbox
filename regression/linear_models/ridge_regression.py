from sklearn import linear_model
import numpy as np

# data for fit
X = [[0,0],[0,0],[1,1]]
y = [0.0,0.1,1.0]

# fit by LinearRegression
model = linear_model.Ridge(alpha=0.5)
model.fit(X,y)

# setting the regularization parameter(generalized cross-validation)
model2 = linear_model.RidgeCV(alphas=np.logspace(start=-6,stop=6,num=13))
model2.fit(X,y)

# print result(coefficient/intercept)
print(model.coef_)
print(model.intercept_)

# print result(alpha)
print(model2.alpha_)

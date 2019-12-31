from sklearn import linear_model

# data for fit
X = [[0,0],[0,0],[1,1]]
y = [0.0,0.1,1.0]

# fit by LinearRegression
model = linear_model.Ridge(alpha=0.5)
model.fit(X,y)

# print result(coefficient/intercept)
print(model.coef_)
print(model.intercept_)

from sklearn import linear_model

# data for fit
X = [[0,0],[1,1],[2,2]]
y = [0,1,2]

# fit by LinearRegression
model = linear_model.LinearRegression()
model.fit(X,y)

# print result(coefficient)
print(model.coef_)

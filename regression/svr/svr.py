from sklearn import svm

# data for fit
X = [[0,0], [2,2]]
y = [0.5, 2.5]

# fit
model = svm.SVR()
model.fit(X,y)

# predict
print(model.predict([[1, 1]]))

from sklearn import svm

# data for fit
X = [[0,0], [2,2]]
y = [0.5, 2.5]

# fit
#model = svm.SVR()
model = svm.SVR(kernel='rbf')
#model = svm.SVR(kernel='linear')
#model = svm.SVR(kernel='sigmoid')
print(model.kernel)
model.fit(X,y)

# predict
print(model.predict([[1, 1]]))

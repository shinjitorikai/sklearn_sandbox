from sklearn import svm

# data for classification
X = [[0,0], [1,1]]
y = [0, 1]

# classify
model = svm.SVC()
model.fit(X,y)

# predict
print(model.predict([[2.0, 2.0]]))

# support vector
print(model.support_vectors_)
# indices of support vectors
print(model.support_)
# number of support vectors for each class
print(model.n_support_)

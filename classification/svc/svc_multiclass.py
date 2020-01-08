from sklearn import svm

# data for classification
X = [[0], [1], [2], [3]]
y = [0, 1, 2, 3]

# classify
model = svm.SVC(decision_function_shape='ovo')
model.fit(X,y)

# predict
print(model.predict([[2.0]]))

# support vector
print(model.support_vectors_)
# indices of support vectors
print(model.support_)
# number of support vectors for each class
print(model.n_support_)

# decision function
decfunc = model.decision_function([[1]])
print(decfunc.shape[1]) # 4class : 4*(4-1)/2=6

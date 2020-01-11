from sklearn.ensemble import RandomForestClassifier

# data for classification
X = [[0,0], [1,1]]
y = [0, 1]

# classify
model = RandomForestClassifier(n_estimators=10)
model.fit(X,y)

# predict
print(model.predict([[1,1]]))

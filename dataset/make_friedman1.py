from sklearn import datasets
import matplotlib.pyplot as plt

# make_friedman1 data
X,y = datasets.make_friedman1(n_samples=100,n_features=5,noise=0.0,random_state=None)
print(X)
print(y)

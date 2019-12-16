from sklearn import datasets
import matplotlib.pyplot as plt

# make_friedman3 data
X,y = datasets.make_friedman3(n_samples=100,noise=0.0,random_state=None)
print(X)
print(y)

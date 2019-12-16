from sklearn import datasets
import matplotlib.pyplot as plt

# make_friedman2 data
X,y = datasets.make_friedman2(n_samples=100,noise=0.0,random_state=None)
print(X)
print(y)

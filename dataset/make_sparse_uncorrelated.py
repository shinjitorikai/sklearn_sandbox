from sklearn import datasets
import matplotlib.pyplot as plt

# make_sparse_uncorrelated data
X,y = datasets.make_sparse_uncorrelated(
    n_samples=100,n_features=10,random_state=None)

print('X = ')
print(X)
print('y = ')
print(y)

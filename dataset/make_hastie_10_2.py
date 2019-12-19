from sklearn import datasets
import matplotlib.pyplot as plt

# make_hastie_10_2 data
X,y = datasets.make_hastie_10_2(n_samples=100,random_state=None)
print(X)
print(y)

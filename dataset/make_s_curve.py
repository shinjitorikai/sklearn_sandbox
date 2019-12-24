from sklearn import datasets
import matplotlib.pyplot as plt

# make_s_curve data
X,y = datasets.make_s_curve(n_samples=100,noise=0.0,random_state=None)
print('X = ')
print(X)
print('y = ')
print(y)

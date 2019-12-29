from sklearn import datasets
import matplotlib.pyplot as plt

# make_swiss_roll data
X,y = datasets.make_swiss_roll(n_samples=100,noise=0.0,random_state=None)

print('X = ')
print(X)
print('y = ')
print(y)

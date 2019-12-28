from sklearn import datasets
import matplotlib.pyplot as plt

# make_spd_matrix data
X = datasets.make_spd_matrix(n_dim=3,random_state=None)

print('X = ')
print(X)

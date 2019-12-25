from sklearn import datasets
import matplotlib.pyplot as plt

# make_sparse_spd_matrix data
prec = datasets.make_sparse_spd_matrix(
    dim=5,alpha=0.95,norm_diag=False,
    smallest_coef=0.1,largest_coef=0.9,
    random_state=None)
print('prec = ')
print(prec)

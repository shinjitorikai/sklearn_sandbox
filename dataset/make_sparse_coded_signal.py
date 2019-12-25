from sklearn import datasets
import matplotlib.pyplot as plt

# make_sparse_coded_signal data
data,dic,code = datasets.make_sparse_coded_signal(
    n_samples=10,n_components=5,n_features=3,n_nonzero_coefs=1,
    random_state=None)
print('data = ')
print(data)
print('dic = ')
print(dic)
print('code = ')
print(code)

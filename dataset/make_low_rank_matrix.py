from sklearn import datasets
import matplotlib.pyplot as plt

# make_low_rank_matrix data
X = datasets.make_low_rank_matrix(n_samples=100,n_features=2,effective_rank=2,tail_strength=0.5,random_state=None)
print(X)

plt.scatter(X[:,0],X[:,1])
plt.show()

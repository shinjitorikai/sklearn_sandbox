from sklearn.neighbors import KDTree
import numpy as np

# data for classification
X = np.array([[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]])

# fit
model = KDTree(X,leaf_size=30,metric='euclidean')

# query the tree for the k nearest neighbors
print(model.query(X,k=2,return_distance=False))

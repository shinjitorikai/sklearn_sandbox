from sklearn.neighbors import NearestNeighbors
import numpy as np

# data for classification
X = np.array([[-1,-1], [-2,-1], [-3,-2], [1,1], [2,1], [3,2]])

# fit
model = NearestNeighbors(n_neighbors=2,algorithm='ball_tree')
nbrs = model.fit(X)

# distance/indices
distance, indices = nbrs.kneighbors(X)
print(distance)
print(indices)

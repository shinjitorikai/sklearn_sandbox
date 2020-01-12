import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

# data for fit
np.random.seed(0)
X = np.sort(5*np.random.rand(40,1),axis=0)
T = np.linspace(0,5,500)[:,np.newaxis]
y = np.sin(X).ravel()

# fit / predict
n_neibors = 5
model = neighbors.KNeighborsRegressor(n_neighbors=n_neibors,weights='uniform')
y_ = model.fit(X,y).predict(T)

# plot result
plt.scatter(X,y,color='darkorange',label='data')
plt.plot(T,y_,color='navy',label='prediction')
plt.legend()
plt.show()

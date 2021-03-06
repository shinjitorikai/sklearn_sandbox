from sklearn import datasets
import matplotlib.pyplot as plt

# make_checkerboard data
X,rows,cols = datasets.make_checkerboard((10,10),4,noise=0.0,minval=10,maxval=100,shuffle=False,random_state=None)
print(X)
print(rows)
print(cols)

# plot dataset
plt.matshow(X)
plt.show()

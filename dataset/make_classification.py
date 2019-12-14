from sklearn import datasets
import matplotlib.pyplot as plt

# make_classification data
X,y = datasets.make_classification(n_samples=100,n_features=2,
    n_informative=1,n_redundant=0,n_repeated=0,n_classes=2,n_clusters_per_class=1,
    weights=None,flip_y=0.01,class_sep=1.0,hypercube=True,shift=0.0,scale=1.0,shuffle=True,random_state=None)
print(X)
print(y)

data0_x, data0_y = X[y==0,0], X[y==0,1]
data1_x, data1_y = X[y==1,0], X[y==1,1]

# plot dataset
plt.scatter(data0_x,data0_y,label='y=0')
plt.scatter(data1_x,data1_y,label='y=1')
plt.grid(which='both')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

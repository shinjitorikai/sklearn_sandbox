from sklearn import datasets
import matplotlib.pyplot as plt

# make_gaussian_quantiles data
X,y = datasets.make_gaussian_quantiles(mean=None,cov=1.0,n_samples=100,
    n_features=2,n_classes=3,shuffle=True,random_state=None)
print(X)
print(y)

data0_x, data0_y = X[y==0,0], X[y==0,1]
data1_x, data1_y = X[y==1,0], X[y==1,1]
data2_x, data2_y = X[y==2,0], X[y==2,1]

# plot dataset
plt.scatter(data0_x,data0_y,label='y=0')
plt.scatter(data1_x,data1_y,label='y=1')
plt.scatter(data2_x,data2_y,label='y=2')
plt.grid(which='both')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

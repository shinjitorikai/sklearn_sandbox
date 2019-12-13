from sklearn import datasets
import matplotlib.pyplot as plt

# make_moons data
X,y = datasets.make_moons(n_samples=200,shuffle=True,noise=0.1,random_state=None)
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

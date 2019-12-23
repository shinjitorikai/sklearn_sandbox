from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# make_regression data
X,y = datasets.make_regression(
    n_samples=100,n_features=2,n_informative=10,
    n_targets=1,bias=0.0,effective_rank=None,
    tail_strength=0.5,noise=0.0,
    shuffle=True,coef=False,random_state=None)

print('X = ')
print(X)
print('y = ')
print(y)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("X3")

ax.plot(X[:,0],X[:,1],y,marker="o",linestyle='None')
plt.show()

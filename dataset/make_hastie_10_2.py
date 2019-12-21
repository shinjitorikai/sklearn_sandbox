from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd

# make_hastie_10_2 data
X,y = datasets.make_hastie_10_2(n_samples=100,random_state=None)
print(X)
print(y)

dataframe = pd.DataFrame(data=X)
datalabel = pd.Series(data=y)
gr = pd.plotting.scatter_matrix(dataframe,c=datalabel,figsize=(12,12))
plt.show()

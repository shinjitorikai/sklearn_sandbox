# train_test_split()によるトレーニング用データ/検証用データの分割

from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# データとラベルの作成
X = np.linspace(0,1,20) # データ
y = 2*X + 3 # ラベル

#plt.scatter(X,y)
#plt.grid(True)
#plt.show()

# トレーニング用データ/検証用データの分割
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8) # トレーニング用データ80%で分割

print('X_train :')
print(X_train)
print('y_train :')
print(y_train)
print('X_test :')
print(X_test)
print('y_test :')
print(y_test)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.scatter(X_train,y_train,label='train',marker='o')
ax1.scatter(X_test,y_test,label='test',marker='+')
ax1.grid(True)
ax1.legend()
plt.show()

from sklearn import datasets
import matplotlib.pyplot as plt

# make_multilabel_classification data
X,y = datasets.make_multilabel_classification(
    n_samples=100,n_features=20,n_classes=5,n_labels=2,
    length=50,allow_unlabeled=True,sparse=False,
    return_indicator='dense',return_distributions=False,
    random_state=None)

print('X = ')
print(X)
print('y = ')
print(y)

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression 
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

x,y = make_classification(n_samples=100, n_features=1, n_informative=1, n_redundant=0,n_classes=2,n_clusters_per_class=1,flip_y=0.01,n_repeated=0)

plt.scatter(x,y,c=y,cmap='rainbow')
plt.title("Scatter plot of Logistic Regression")
plt.show()

x_train,y_train,x_test,y_test = train_test_split(x,y,random_state=1)

log_reg = LogisticRegression()
log_reg.fit(x_train,y_train)

print(log_reg.coef_)
print(log_reg.intercept_)

y_pred = log_reg.predict(x_test)

print(y_pred)
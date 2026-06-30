from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()
x = iris.data[:,:2]
y = iris.target
logreg = LogisticRegression(max_iter=200)

logreg.fit(x,y)

x_min,x_max = x[:,0].min() - .5,x[:,0].max() + 5
y_min,y_max = x[:,1].min() - .5,x[:,1].max() + 5
h = .02
xx,yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

z = z.reshape(xx.shape)
plt.figure(1,figsize=(4,3))
plt.pcolormesh(xx,yy,z,cmap=plt.cm.Paired)

plt.scatter(x[:,0],x[:,1], c=y, edgecolors = 'k',cmap=plt.cm.Paired)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal width")

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(),yy.max())
plt.xticks(())
plt.yticks(())

plt.show()
logreg.score(x,y)
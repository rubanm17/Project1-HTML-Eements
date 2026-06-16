import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("xydataset.csv", header=None)

X = data.iloc[:,0].values
Y = data.iloc[:,1].values

m = 0
b = 0

learning_rate = 0.0001
iterations = 1000

n = len(X)

for i in range(iterations):

    Y_pred = m * X + b

    dm = (-2/n) * np.sum(X * (Y - Y_pred))
    db = (-2/n) * np.sum(Y - Y_pred)

    m = m - learning_rate * dm
    b = b - learning_rate * db

print("Slope (m):", m)
print("Intercept (b):", b)

Y_pred = m * X + b

plt.scatter(X, Y, color='black')
plt.plot(X, Y_pred, color='blue')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression using Gradient Descent")

plt.show()
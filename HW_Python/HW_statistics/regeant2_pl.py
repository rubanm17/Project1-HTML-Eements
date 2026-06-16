import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X_train = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(-1,1)
y_train = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5])

X_test = np.array([10,11,12,13,14]).reshape(-1,1)
y_test = np.array([5,5.5,7,6.5,7])

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)

plt.scatter(X_train, y_train, color='black', label='Training Data')

plt.plot(X_train,
         model.predict(X_train),
         color='blue',
         linewidth=2,
         label='Regression Line')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()

plt.show()
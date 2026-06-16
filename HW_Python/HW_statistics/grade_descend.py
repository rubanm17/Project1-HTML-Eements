import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("xydataset.csv")

X = df.iloc[:, 1].values.reshape(-1, 1)
y = df.iloc[:, 2].values

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))

plt.scatter(X, y, color='black', label='Data Points')
plt.plot(X, y_pred, color='blue', linewidth=2, label='Regression Line')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Plot")
plt.legend()

plt.show()
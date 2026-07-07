import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.read_csv("unconv_MV_v5 (1).csv")

print(df.head())

X = df[['Por', 'Brittle', 'Perm', 'TOC']]
y = df['Prod']

print("\nMissing Values:")
print(df.isnull().sum())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Evaluation")
print("----------------")
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))

print("\nModel Coefficients")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")

print("\nIntercept:", model.intercept_)

new_data = pd.DataFrame({
    'Por': [10],
    'Brittle': [50],
    'Perm': [100],
    'TOC': [3]
})

prediction = model.predict(new_data)
print("\nPredicted Production:", prediction[0])
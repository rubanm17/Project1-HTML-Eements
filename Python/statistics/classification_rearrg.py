import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("inc.csv")
print(df.head())
plt.scatter(df.age,df.bought_insurance,marker='+',color="red")
x_train,x_test,y_train,y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)
print(x_test)
model = LogisticRegression()
model.fit(x_train,y_train)
print(x_test)
y_pred = model.predict(x_test)
model.predict_proba(x_test)
model.score(x_test,y_test)
print(y_pred)
print(x_test)
print(model.coef_)
print(model.intercept_)
import math
def sigmoid(x):
    return 1/(1+math.exp(-x))
def prediction(age):
    z = 0.042 * age - 1.53
    y = sigmoid(z)
    return y

Age = 35
prediction(Age)

Age = 45
prediction(Age)
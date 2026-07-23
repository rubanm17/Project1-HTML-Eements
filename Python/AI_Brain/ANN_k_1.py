import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Churn.csv")
print(df.head())
print(df.info())
print(df.describe())

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

print(df)
print(df.info())

df = df.drop(['RowNumber','CustomerId','Surname'],axis=1)

print(df.shape)
x = df
y = df.pop('Exited')

print(x.shape)
print(y.shape)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

print(x_train)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tin = pd.read_csv('titanic.csv', sep = "\t")
print(tin.head())
tin.shape
tin.isnull().sum()
sns.heatmap(tin.isnull(), cmap='spring')
print(tin.head())
tin.dropna(inplace=True)
sns.heatmap(tin.isnull(), cbar=False)
tin.isnull().sum()

pd.get_dummies(tin["Sex"]).head()
sine = pd.get_dummies(tin['Sex'],drop_first=True)
print(sine.head(4))

pd.get_dummies(tin['Embarked']).head(4)
arked = pd.get_dummies(tin['Embarked'],drop_first=True)

pclass = pd.get_dummies(tin['Pclass'],drop_first=True)
print(pclass.head(4))

Titanic = pd.concat([tin, sine, pclass], axis=1)
print(Titanic.head())   
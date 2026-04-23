import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic_Dataset.csv')
data.head(5)
data.isnull().sum()

plt.boxplot(data['Age'])
plt.title('Age Distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Pclass Distribution')
plt.show()

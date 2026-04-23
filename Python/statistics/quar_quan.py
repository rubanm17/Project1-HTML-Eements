import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic_Dataset.csv')

data.head(5)

data.isnull().sum()

age_q1 = np.quantile(data['Age'], 0.25)
age_q2 = np.quantile(data['Age'], 0.5)
age_q3 = np.quantile(data['Age'], 0.75)
print("Q1:",age_q1)
print("Q2:",age_q2)
print("Q3:",age_q3)
IQR = age_q3 - age_q1
print("Inter quantile range:",IQR)
plt.hist(data['Age'])
plt.ylabel('Count of passengers')
plt.xlabel('Age')
plt.show()
fare_q1 = np.quantile(data['Fare'], 0.25)
fare_q2 = np.quantile(data['Fare'], 0.5)
fare_q3 = np.quantile(data['Fare'], 0.75)
print("Q1:",fare_q1)
print("Q2:",fare_q2)
print("Q3:",fare_q3)
IQR_fare = fare_q3 - fare_q1
print("Inter quantile range:",IQR_fare)
bins = np.arange(0,250,20)
plt.hist(data['Fare'], bins=np.arange(0,250,20))
plt.ylabel('Count of passengers')
plt.xlabel('Fare')
plt.show()

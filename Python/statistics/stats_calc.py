import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data = pd.read_csv('Titanic_Dataset.csv')
data.head()

mean_age = np.mean(data['Age'])
print("Mean age of passengers:", mean_age)

mean_fare = np.mean(data['Fare'])
print("Mean fare of passengers:", mean_fare)

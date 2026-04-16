import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics as stats

data = pd.read_csv('Titanic_Dataset.csv')
data.head()

median_age = np.median(data['Age'])
print("Median age of passengers:", median_age)

median_fare = np.median(data['Fare'])
print("Median fare of passengers:", median_fare)

mode_age = stats.mode(data['Age'])
print("Mode age of passengers:", mode_age)

mode_clas = stats.mode(data['Pclass'])
print("Mode class of passengers:", mode_clas)

mode_gender = data['Gender'].value_counts().index[0]
print("Mode of features Gender: ", mode_gender)
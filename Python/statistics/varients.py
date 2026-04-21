import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('climate_record.csv')

data.head(5)
data.info()
data.isnull().sum()
mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature:", mean_temp)
var_temp = np.var(data['Temperature (C)'])
print("Variance of Temperature:", var_temp)
std_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation of Temperature:", std_deviation_temp)

for i in range(1,13):
    month = data.loc[data['Month'] == i]["Temperature (C)"]
    print("For month"+str(i))
    print("Mean Temperature:" + str(np.mean(month)))
    print("Standard deviation is" + str(np.std(month))+"\n")
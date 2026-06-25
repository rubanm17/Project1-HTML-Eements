import numpy as np
import seaborn as sns
import pandas as pd

dataset = pd.read_csv("glass.csv")

sns.set_style('dark')
import matplotlib.pyplot as plt
plt.rcParams.update({"figure.figsize":(8,6),"axes.titlepad":22.0})

print("Target variables:", dataset['target_names'])

(unique, counts) = np.unique(dataset['target'], return_counts=True)

print("Unique variable counts:", unique)
print("Counts:", counts)

sns.barplot(x=dataset['target_names'],y=counts)
plt.title("Target Variable Counts")
plt.show()
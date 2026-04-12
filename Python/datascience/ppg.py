import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

HouseDF = pd.read_csv('USA_DESTRUCTION.csv')

HouseDF.head()

HouseDF.info()

HouseDF.columns

sns.pairplot(HouseDF)

sns.heatmap(HouseDF.corr(),annot=True)
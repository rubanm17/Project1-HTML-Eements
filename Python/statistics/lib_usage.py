import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np


data = pd.read_csv('Titanic_Dataset.csv')
data.head(5)

data.dtypes

data.isnull().sum()

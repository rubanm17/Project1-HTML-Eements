import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Rate_movie.csv')
data.head(5)
data.isnull().sum()

plt.hist(data['Runtime'])
plt.xlabel('Count of movies')
plt.ylabel('Runtime')
plt.show()
plt.hist(data['IMDB_Rating'])
plt.xlabel('Count of movies')
plt.ylabel('IMDB_Rating')
data['Runtime'].unique()
bins_time = np.arange(80,230,10)
plt.show()
plt.hist(data['Runtime'], edgecolor='black', bins=bins_time,color='g')
plt.xlabel('Runtime')
plt.ylabel('Count of movies')
data['IMDB_Rating'].unique()
bins_rating = np.arange(8,10,0.20)
plt.show()
plt.hist(data['IMDB_Rating'], edgecolor='black', bins=bins_rating,color='g')
plt.xlabel('IMDB_Rating')
plt.ylabel('Count of movies')
plt.xticks(bins_rating)
plt.show()
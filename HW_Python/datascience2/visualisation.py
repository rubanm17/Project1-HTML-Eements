import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Import dataset
df = pd.read_csv('TipsDataset.csv')

# Display basic info
print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)

# 2. Distribution of features (size, tip, total_bill)
sns.histplot(df['total_bill'], kde=True)
plt.title('Total Bill Distribution')
plt.show()

sns.histplot(df['tip'], kde=True)
plt.title('Tip Distribution')
plt.show()

sns.histplot(df['size'], kde=True)
plt.title('Size Distribution')
plt.show()

# 3. Histogram for total_bill with KDE
sns.histplot(df['total_bill'], kde=True, bins=20)
plt.title('Histogram of Total Bill with KDE')
plt.show()

# 4. Scatter plot (total_bill vs tip, hue = time)
sns.scatterplot(x='total_bill', y='tip', hue='time', data=df)
plt.title('Total Bill vs Tip (Time as Hue)')
plt.show()

# 5. Pair plot with gender as hue (sex column)
df['gender'] = df['gender'].astype(str)
sns.pairplot(df, hue='gender')

plt.show()
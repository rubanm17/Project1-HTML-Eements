# -------------------------------
# Import Libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Dataset
# -------------------------------
data = pd.read_csv('Bestsellers_with_categories1.csv')

print(data.head())

# -------------------------------
# 1. Check null values
# -------------------------------
print("\nNull Values:\n", data.isnull().sum())

# -------------------------------
# 2. Handle missing values
# -------------------------------
# Numerical → median
for col in data.select_dtypes(include=np.number).columns:
    data[col].fillna(data[col].median(), inplace=True)

# Categorical → mode
for col in data.select_dtypes(include='object').columns:
    data[col].fillna(data[col].mode()[0], inplace=True)

print("\nAfter Handling Missing Values:\n", data.isnull().sum())

# -------------------------------
# 3. Check need for combining categories
# -------------------------------
print("\nGenre Value Counts:\n", data['Genre'].value_counts())

# (Optional) Combine if needed
# Example (if too many categories)
# data['Genre'] = data['Genre'].replace({'Self Help':'Non Fiction'})

# -------------------------------
# 4. Bin User Rating into categories
# -------------------------------
bins = [0, 4.5, 5]
labels = ['Good', 'Excellent']

data['Rating_Category'] = pd.cut(data['User Rating'], bins=bins, labels=labels)

print("\nBinned Ratings:\n", data[['User Rating','Rating_Category']].head())

# Bar Plot
data['Rating_Category'].value_counts().plot(kind='bar')
plt.title("User Rating Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# -------------------------------
# 5. Skewness of numerical features
# -------------------------------
num_cols = data.select_dtypes(include=np.number).columns

for col in num_cols:
    print(f"\nDistribution of {col}")
    sns.histplot(data[col], kde=True)
    plt.show()
    
    print("Skewness -", data[col].skew())

# -------------------------------
# 6. Association: User Rating vs Genre
# -------------------------------
sns.boxplot(data=data, x='Genre', y='User Rating')
plt.title("User Rating vs Genre")
plt.show()

# -------------------------------
# 7. Association: User Rating vs Price
# -------------------------------
plt.scatter(data['Price'], data['User Rating'])
plt.xlabel("Price")
plt.ylabel("User Rating")
plt.title("User Rating vs Price")
plt.show()

# -------------------------------
# Extra: Categorical Association
# -------------------------------
assoc = pd.crosstab(data['Genre'], data['Rating_Category'])
print("\nCategorical Association:\n", assoc)
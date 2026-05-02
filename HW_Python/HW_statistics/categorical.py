import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('Bestsellers_with_categories.csv')

# Preview data
print(data.head())

# -------------------------------
# 1. Check null values
# -------------------------------
print("\nNull Values:\n", data.isnull().sum())

# -------------------------------
# 2. Handle missing values
# -------------------------------
# Fill numerical columns with median
for col in data.select_dtypes(include=np.number).columns:
    data[col].fillna(data[col].median(), inplace=True)

# Fill categorical columns with mode
for col in data.select_dtypes(include='object').columns:
    data[col].fillna(data[col].mode()[0], inplace=True)

print("\nAfter Handling Missing Values:\n", data.isnull().sum())

# -------------------------------
# 3. Frequency of Genre
# -------------------------------
print("\nGenre Frequency:\n", data['Genre'].value_counts())

# -------------------------------
# 4. Median of Genre (Categorical)
# -------------------------------
genre_categories = data['Genre'].unique().tolist()
data['Genre'] = pd.Categorical(data['Genre'], categories=genre_categories, ordered=True)

median_index = int(np.median(data['Genre'].cat.codes))
median_genre = genre_categories[median_index]

print("\nMedian Genre:", median_genre)

# -------------------------------
# 5. Bar Chart & Pie Chart
# -------------------------------
# Bar Chart
plt.figure()
data['Genre'].value_counts().plot(kind='bar')
plt.title("Genre Distribution (Bar Chart)")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# Pie Chart
plt.figure()
data['Genre'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Genre Distribution (Pie Chart)")
plt.ylabel('')
plt.show()

# -------------------------------
# 6. Numerical DataFrame + Boxplot
# -------------------------------
num_df = data.select_dtypes(include=np.number)

print("\nNumerical Columns:\n", num_df.columns)

plt.figure()
sns.boxplot(data=num_df)
plt.title("Boxplot of Numerical Features")
plt.show()

# -------------------------------
# 7. Normalization / Standardization
# -------------------------------
# If outliers present → Standardization
# If not → Normalization

# Standardization (Z-score)
standardized_df = (num_df - num_df.mean()) / num_df.std()

print("\nStandardized Data Sample:\n", standardized_df.head())

# OR Normalization (Min-Max)
normalized_df = (num_df - num_df.min()) / (num_df.max() - num_df.min())

print("\nNormalized Data Sample:\n", normalized_df.head())
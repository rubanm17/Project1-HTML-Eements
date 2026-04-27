import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('Bestsellerswith_categories.csv')

# 1. Check null values
print("Null values:\n", data.isnull().sum())

# 2. Handle missing values (if any)
# Option 1: Drop missing rows
data = data.dropna()

# (OR you can use fillna if needed)
# data['Price'].fillna(data['Price'].mean(), inplace=True)

# 3. Find value that divides 10% of data (10th percentile) for Price
price_10_percentile = np.percentile(data['Price'], 10)
print("10% value (Price):", price_10_percentile)

# 4. Quartiles and IQR for Price
Q1_price = np.percentile(data['Price'], 25)
Q2_price = np.percentile(data['Price'], 50)  # Median
Q3_price = np.percentile(data['Price'], 75)
IQR_price = Q3_price - Q1_price

print("\nPrice Quartiles:")
print("Q1:", Q1_price, "Q2:", Q2_price, "Q3:", Q3_price)
print("IQR (Price):", IQR_price)

# 5. Quartiles and IQR for User Rating
Q1_rating = np.percentile(data['User Rating'], 25)
Q2_rating = np.percentile(data['User Rating'], 50)
Q3_rating = np.percentile(data['User Rating'], 75)
IQR_rating = Q3_rating - Q1_rating

print("\nUser Rating Quartiles:")
print("Q1:", Q1_rating, "Q2:", Q2_rating, "Q3:", Q3_rating)
print("IQR (User Rating):", IQR_rating)

# 6. Boxplots

# Price Boxplot
plt.boxplot(data['Price'])
plt.title('Price Distribution')
plt.ylabel('Price')
plt.show()

# User Rating Boxplot
plt.boxplot(data['User Rating'])
plt.title('User Rating Distribution')
plt.ylabel('Rating')
plt.show()
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# Load Dataset
# -----------------------------------
data = pd.read_csv('Bestsellerswithcategories.csv')

# Display first rows
print(data.head(5))

# -----------------------------------
# Check Null Values
# -----------------------------------
print(data.isnull().sum())

# -----------------------------------
# Handle Missing Values
# -----------------------------------
data['User Rating'] = data['User Rating'].fillna(data['User Rating'].mean())
data['Price'] = data['Price'].fillna(data['Price'].mean())

# -----------------------------------
# Variance & Standard Deviation
# -----------------------------------
print("\nUser Rating Variance:", data['User Rating'].var())
print("User Rating Std Dev:", data['User Rating'].std())

print("\nPrice Variance:", data['Price'].var())
print("Price Std Dev:", data['Price'].std())

# -----------------------------------
# Histogram - User Rating (Basic)
# -----------------------------------
plt.hist(data['User Rating'])
plt.xlabel('User Rating')
plt.ylabel('Count of Books')
plt.show()

# -----------------------------------
# Histogram - Price (Basic)
# -----------------------------------
plt.hist(data['Price'])
plt.xlabel('Price')
plt.ylabel('Count of Books')
plt.show()

# -----------------------------------
# Custom Histogram - User Rating
# -----------------------------------
data['User Rating'].unique()

bins_rating = np.arange(3.0, 5.1, 0.2)

plt.hist(data['User Rating'], edgecolor='black', bins=bins_rating, color='g')
plt.xlabel('User Rating')
plt.ylabel('Count of Books')
plt.xticks(bins_rating)
plt.show()

# -----------------------------------
# Custom Histogram - Price
# -----------------------------------
data['Price'].unique()

bins_price = np.arange(0, 250, 20)

plt.hist(data['Price'], edgecolor='black', bins=bins_price, color='g')
plt.xlabel('Price')
plt.ylabel('Count of Books')
plt.show()
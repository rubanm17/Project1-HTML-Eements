# Import Libraries
import pandas as pd
import numpy as np

# -----------------------------------
# 1. Load Dataset
# -----------------------------------
df = pd.read_csv("Bestsellers_categories.csv")

# -----------------------------------
# 2. Check Quantitative & Categorical Features
# -----------------------------------
print("All Columns:\n", df.columns)

print("\nNumerical Columns:")
print(df.select_dtypes(include=np.number).columns)

print("\nCategorical Columns:")
print(df.select_dtypes(include='object').columns)

# -----------------------------------
# 3. Check Null Values
# -----------------------------------
print("\nNull Values Count:\n", df.isnull().sum())

# -----------------------------------
# 4. Handle Missing Values
# -----------------------------------

# Numerical → mean
num_cols = ['User Rating', 'Reviews', 'Price']

for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# Categorical → mode
cat_cols = ['Name', 'Author', 'Genre']

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------------
# 5. Custom Functions (Inspired from stats_calc.py)
# -----------------------------------

def calculate_stats(series):
    data = list(series)

    # Mean
    mean_val = sum(data) / len(data)

    # Median
    sorted_data = sorted(data)
    n = len(data)

    if n % 2 == 0:
        median_val = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median_val = sorted_data[n//2]

    # Mode
    mode_val = max(set(data), key=data.count)

    return mean_val, median_val, mode_val

# -----------------------------------
# 6. User Rating Stats
# -----------------------------------
mean_u, median_u, mode_u = calculate_stats(df['User Rating'])

print("\nUser Rating:")
print("Mean:", mean_u)
print("Median:", median_u)
print("Mode:", mode_u)

# -----------------------------------
# 7. Price Stats
# -----------------------------------
mean_p, median_p, mode_p = calculate_stats(df['Price'])

print("\nPrice:")
print("Mean:", mean_p)
print("Median:", median_p)
print("Mode:", mode_p)

# -----------------------------------
# 8. Reviews Stats
# -----------------------------------
mean_r, median_r, mode_r = calculate_stats(df['Reviews'])

print("\nReviews:")
print("Mean:", mean_r)
print("Median:", median_r)
print("Mode:", mode_r)
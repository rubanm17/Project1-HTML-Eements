import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv('PenguinsData.csv')

# View first rows
print(df.head(10))

# 1. Check if any null values are present
print("\nAny Null Values?\n", df.isnull().any())

# 2. Total number of null values in each column
print("\nNull Values Count per Column:\n", df.isnull().sum())

# 3. Visualize null values
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Null Values Heatmap")
plt.show()

# 4. Handle categorical null values (mode)
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nAfter categorical handling:\n", df[categorical_cols].isnull().sum())

# 5. Handle numerical null values (mean)
numerical_cols = df.select_dtypes(include=np.number).columns
for col in numerical_cols:
    df[col].fillna(df[col].mean(), inplace=True)

print("\nAfter numerical handling:\n", df[numerical_cols].isnull().sum())

# Final null check
print("\nFinal Null Check:\n", df.isnull().sum())

# Additional methods (corrected)
df_drop_all_null = df.dropna(how='all')
df_forward_fill = df.ffill()
df_backward_fill = df.bfill()

# ✅ FIXED interpolation (only numeric columns)
df[numerical_cols] = df[numerical_cols].interpolate()

print("\nCompleted all operations successfully")
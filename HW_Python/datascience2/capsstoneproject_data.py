# Load Basic Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# -----------------------------------
# 1. Load Dataset
# -----------------------------------
df = pd.read_csv("PenguinsDatacaps.csv")

# -----------------------------------
# 2. Basic Info
# -----------------------------------
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.info())

# -----------------------------------
# 3. Check Null Values
# -----------------------------------
print("Null Values Count:\n", df.isnull().sum())

# -----------------------------------
# 4. Visualize Null Values
# -----------------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Null Values Heatmap")
plt.show()

# -----------------------------------
# 5. Handle Missing Values
# -----------------------------------

# Numerical columns → fill with mean
num_cols = ['Culmen Length (mm)', 'Culmen Depth (mm)', 
            'Flipper Length (mm)', 'Body Mass (g)']

for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# Categorical columns → fill with mode
cat_cols = ['Species', 'Island', 'Gender']

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------------
# 6. Pair Plot (Numerical Features)
# -----------------------------------
sns.pairplot(df[num_cols])
plt.show()

# -----------------------------------
# 7. Correlation Heatmap
# -----------------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------------
# 8. Boxplot for Numerical Features
# -----------------------------------
df[num_cols].plot(kind='box', subplots=True, layout=(2,2), figsize=(10,8))
plt.suptitle("Boxplots of Numerical Features")
plt.show()

# -----------------------------------
# 9. Count Plot for Gender
# -----------------------------------
sns.countplot(x='Gender', data=df)
plt.title("Count Plot of Gender")
plt.show()
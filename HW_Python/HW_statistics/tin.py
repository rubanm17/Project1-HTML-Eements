# ==========================================
# TITANIC DATA PREPROCESSING AND CLASSIFICATION
# ==========================================

# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic.csv')

print("First 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nNull Values Before Cleaning:")
print(df.isnull().sum())

plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

df['Age'].fillna(df['Age'].median(), inplace=True)

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.drop('Cabin', axis=1, inplace=True)

print("\nNull Values After Cleaning:")
print(df.isnull().sum())

plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df)
plt.title("Survived vs Dead People")
plt.xlabel("0 = Dead, 1 = Survived")
plt.ylabel("Number of Passengers")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Based on Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

survived_people = df[df['Survived'] == 1]

plt.figure(figsize=(6,4))
sns.countplot(x='Sex', data=survived_people)
plt.title("Survived Males and Females")
plt.xlabel("Gender")
plt.ylabel("Number of Survivors")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival Based on Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()
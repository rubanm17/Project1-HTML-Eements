import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (make sure file name is correct)
df = pd.read_csv('PenguinsDatahw.csv')

# Check columns (optional)
print(df.columns)

# Drop null values for clean plotting
df = df.dropna()

# -----------------------------------
# 1. Scatter Plot: Culmen Length vs Body Mass
# -----------------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['Culmen Length (mm)'], df['Body Mass (g)'])
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Scatter Plot: Culmen Length vs Body Mass')
plt.show()

# -----------------------------------
# 2. Scatter Plot: Culmen Depth vs Body Mass
# -----------------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['Culmen Depth (mm)'], df['Body Mass (g)'])
plt.xlabel('Culmen Depth (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Scatter Plot: Culmen Depth vs Body Mass')
plt.show()

# -----------------------------------
# 3. Pair Plot (All Features)
# -----------------------------------
sns.pairplot(df[['Culmen Length (mm)', 
                 'Culmen Depth (mm)', 
                 'Flipper Length (mm)', 
                 'Body Mass (g)']])
plt.show()

# -----------------------------------
# 4. Area Graph: Culmen Length vs Body Mass
# -----------------------------------
plt.figure(figsize=(8,5))

# Sort values for proper area graph
df_sorted = df.sort_values('Culmen Length (mm)')

plt.fill_between(df_sorted['Culmen Length (mm)'],
                 df_sorted['Body Mass (g)'],
                 alpha=0.5)

plt.xlabel('Culmen Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Area Graph: Culmen Length vs Body Mass')
plt.show()
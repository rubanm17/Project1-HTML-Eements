import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('PenguinsData1.csv')

# Use EXACT column names (with spaces and brackets)
culmen_length = df['Culmen Length (mm)'].dropna()
culmen_depth = df['Culmen Depth (mm)'].dropna()
flipper_length = df['Flipper Length (mm)'].dropna()
body_mass = df['Body Mass (g)'].dropna()

# Same style as your sample
type = [culmen_length, culmen_depth, flipper_length, body_mass]

colors = ['g', 'r', 'b', 'y']
label = ['Culmen Length', 'Culmen Depth', 'Flipper Length', 'Body Mass']

bins = [0, 50, 100, 150, 200, 300, 6000]

plt.xlabel("Penguin Features")
plt.ylabel("Count")

plt.hist(type,
         bins=bins,
         rwidth=0.95,
         color=colors,
         label=label,
         orientation="horizontal")

plt.legend()
plt.title("Histogram of Penguin Data")
plt.show()
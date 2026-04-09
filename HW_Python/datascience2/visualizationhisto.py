import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Penguins_Data.csv')

# Extract features (drop nulls for clean plotting)
culmen_length = df['culmen_length_mm'].dropna()
culmen_depth = df['culmen_depth_mm'].dropna()
flipper_length = df['flipper_length_mm'].dropna()
body_mass = df['body_mass_g'].dropna()

# Combine like your example
data = [culmen_length, culmen_depth, flipper_length, body_mass]

# Labels and colors
labels = ['Culmen Length', 'Culmen Depth', 'Flipper Length', 'Body Mass']
colors = ['g', 'r', 'b', 'y']

# Custom bins (adjusted for penguins data)
bins = [0, 50, 100, 150, 200, 300, 6000]

# Labels
plt.xlabel("Penguin Measurements")
plt.ylabel("Count")

# Histogram (same style as your sample)
plt.hist(data, bins=bins, rwidth=0.9, color=colors, label=labels)

plt.legend()
plt.title("Histogram of Penguin Features")
plt.show()
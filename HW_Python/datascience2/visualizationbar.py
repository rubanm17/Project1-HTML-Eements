import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create July DataFrame
july = pd.DataFrame({
    'Day': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    'Births': [12, 15, 11, 9, 1, 9, 21]
})

# Create August DataFrame
august = pd.DataFrame({
    'Day': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    'Births': [17, 5, 2, 11, 1, 8, 29]
})

# Merge both datasets (like your example)
data = july.merge(august, on='Day', suffixes=('_July', '_August'))

print(data)

# Sort by July births (optional, like your code style)
data = data.sort_values('Births_July', ascending=False)

days = data['Day']
july_vals = data['Births_July']
aug_vals = data['Births_August']

# Create bar positions
x = np.arange(len(days))

plt.figure(figsize=(15, 8))

# Plot bars (same style)
plt.bar(x - 0.2, july_vals, width=0.4, color='blue', edgecolor='black', label='July')
plt.bar(x + 0.2, aug_vals, width=0.4, color='red', edgecolor='black', label='August')

# Labels and title
plt.xlabel('Days')
plt.ylabel('Number of Births')
plt.title('Comparison of Birth Rate (July vs August)')
plt.xticks(x, days, rotation=45)

# Add value labels (same as your annotate style)
for i in range(len(days)):
    plt.annotate(july_vals.iloc[i],
                 (x[i] - 0.2, july_vals.iloc[i]),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

    plt.annotate(aug_vals.iloc[i],
                 (x[i] + 0.2, aug_vals.iloc[i]),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')

plt.legend()
plt.show()
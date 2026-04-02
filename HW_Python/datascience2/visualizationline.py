import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Create July data
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
july_births = [12, 15, 11, 9, 1, 9, 21]

df_july = pd.DataFrame({
    'Day': days,
    'New Births': july_births
})

print("July Data:\n", df_july)

# Line plot for July
plt.plot(df_july['Day'], df_july['New Births'],
         linestyle='dashed', marker='o', linewidth=2, label='July Births')

plt.xlabel('Days')
plt.ylabel('New Births')
plt.title('Birth Rate - July')
plt.legend()
plt.show()


# 3. Create August data
aug_births = [17, 5, 2, 11, 1, 8, 29]

df_aug = pd.DataFrame({
    'Day': days,
    'New Births': aug_births
})

print("\nAugust Data:\n", df_aug)

# Line plot for August
plt.plot(df_aug['Day'], df_aug['New Births'],
         linestyle='solid', marker='D', linewidth=2, label='August Births')

plt.xlabel('Days')
plt.ylabel('New Births')
plt.title('Birth Rate - August')
plt.legend()
plt.show()


# 5. Compare both months
plt.plot(days, july_births,
         linestyle='dashed', marker='o', linewidth=2, label='July')

plt.plot(days, aug_births,
         linestyle='solid', marker='D', linewidth=2, label='August')

plt.xlabel('Days')
plt.ylabel('New Births')
plt.title('Comparison of Birth Rates (July vs August)')
plt.legend()
plt.show()


# 6. Solve equation y = 6x^2 + x + 1
x = np.arange(1, 11)
y = (6 * x**2) + x + 1

plt.plot(x, y, 'g', linewidth=3, marker='o', label='y = 6x^2 + x + 1')

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Graph of y = 6x^2 + x + 1')
plt.legend()
plt.show()
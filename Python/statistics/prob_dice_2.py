import numpy as np

die_sides = int(input("Enter the number of sides in the dice:"))
die = range(1,die_sides)

num_rolls = int(input("Enter the number of rolls:"))

res = np.random.choice(die, size=num_rolls,replace=True)
print(res)
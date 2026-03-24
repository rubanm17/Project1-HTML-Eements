import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='ticks')

# 1. Import dataset
iris = pd.read_csv('IrisDataset.csv')

print(iris.head())
print(iris.info())

# Fix column names (important)
iris.columns = iris.columns.str.strip()

# 2. Barplot: Species vs SepalLengthCm
sns.barplot(x=iris['Species'], y=iris['SepalLengthCm'])
plt.show()

# 3. Count plot for Species
sns.countplot(x=iris['Species'])
plt.show()

# 4. Boxplot: Species vs SepalWidthCm
sns.boxplot(x=iris['Species'], y=iris['SepalWidthCm'])
plt.show()

# 5. Swarm plot: Species vs SepalWidthCm
sns.swarmplot(x=iris['Species'], y=iris['SepalWidthCm'])
plt.show()

# 6. Distribution of SepalWidthCm
sns.histplot(iris['SepalWidthCm'])
plt.show()

sns.histplot(iris['SepalWidthCm'], kde=True)
plt.show()

sns.jointplot(x=iris['SepalWidthCm'], y=iris['SepalLengthCm'])
plt.show()

# 7. Pairplot with Species as hue
sns.pairplot(iris, hue='Species')
plt.show()
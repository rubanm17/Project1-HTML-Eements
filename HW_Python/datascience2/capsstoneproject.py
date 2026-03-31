import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load dataset (replace path if needed)
df = pd.read_csv('IMDBDataset.csv')

# 1. Import dataset
print("Dataset Loaded Successfully\n")

# 2. First 3 and Last 3 rows
print("First 3 rows:\n", df.head(3))
print("\nLast 3 rows:\n", df.tail(3))

# 3. Detailed information
print("\nDataset Info:\n")
print(df.info())

print("\nData Types:\n", df.dtypes)

print("\nStatistical Summary:\n", df.describe(include='all'))

# 4. Check null values
print("\nNull Values:\n", df.isnull().sum())

# 5. Subset rows (41 to 75)
subset_df = df.iloc[40:75]
print("\nSubset (Rows 41 to 75):\n", subset_df)

# 6. Movie with highest votes
# (Assuming column name is 'Votes')
if 'No_of_Votes' in df.columns:
    max_votes_movie = df.loc[df['No_of_Votes'].idxmax()]
    print("\nMovie with Highest Votes:\n", max_votes_movie)
else:
    print("\nColumn 'Votes' not found in dataset")

# 7. Boxplot for IMDB_Rating and Runtime
if 'IMDB_Rating' in df.columns and 'Runtime' in df.columns:
    df[['IMDB_Rating', 'Runtime']].plot(kind='box', subplots=True, layout=(1,2), figsize=(8,5))
    plt.show()

# 8. Relationship between IMDB_Rating and Runtime
if 'IMDB_Rating' in df.columns and 'Runtime' in df.columns:
    plt.scatter(df['Runtime'], df['IMDB_Rating'])
    plt.xlabel('Runtime')
    plt.ylabel('IMDB Rating')
    plt.title('IMDB Rating vs Runtime')
    plt.show()

# 9. Distribution of IMDB_Rating and Runtime
if 'IMDB_Rating' in df.columns and 'Runtime' in df.columns:
    df[['IMDB_Rating', 'Runtime']].hist(figsize=(10,5))
    plt.show()

# 10. Count plot of Rating
# (Assuming column name is 'Rating' or similar)
if 'Rating' in df.columns:
    sns.countplot(data=df, x='Rating')
    plt.xticks(rotation=90)
    plt.show()
elif 'IMDB_Rating' in df.columns:
    sns.countplot(data=df, x='IMDB_Rating')
    plt.xticks(rotation=90)
    plt.show()

# Additional: Correlation Heatmap (like your example)
numeric_df = df.select_dtypes(include=[np.number])
if not numeric_df.empty:
    sns.heatmap(numeric_df.corr(), annot=True)
    plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

print("Null Values in Matches Dataset:")
print(matches.isnull().sum())

plt.figure(figsize=(10,6))
sns.heatmap(matches.isnull(), cbar=False, yticklabels=False)
plt.title("Missing Values - Matches Dataset")
plt.show()

matches.drop('umpire3', axis=1, inplace=True)

matches_clean = matches.dropna()

print("\nMatches Dataset Shape After Cleaning:")
print(matches_clean.shape)

print("\nNull Values in Deliveries Dataset:")
print(deliveries.isnull().sum())

plt.figure(figsize=(10,6))
sns.heatmap(deliveries.isnull(), cbar=False, yticklabels=False)
plt.title("Missing Values - Deliveries Dataset")
plt.show()

deliveries['player_dismissed'] = deliveries['player_dismissed'].fillna('Not Out')
deliveries['dismissal_kind'] = deliveries['dismissal_kind'].fillna('None')
deliveries['fielder'] = deliveries['fielder'].fillna('None')

print("\nNull Values After Cleaning:")
print(deliveries.isnull().sum())

merged_data = pd.merge(
    matches_clean,
    deliveries,
    left_on='id',
    right_on='match_id',
    how='inner'
)

print("\nMerged Dataset Shape:")
print(merged_data.shape)

print("\nFirst 5 Rows of Merged Dataset:")
print(merged_data.head())
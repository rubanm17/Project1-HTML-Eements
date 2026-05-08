import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as plt

data = pd.read_csv('Titanic_Dataset.csv')
data.head(5)

data.dtypes

nominal_cat = ['Name','Ticket','Cabin']

original_cat = ['Embarked','Gender']

data['Gender'].value_counts()
gender_categories = ['Male','Female']
data['Gender'] = pd.Categorical(data['Gender'],gender_categories,ordered = True)
median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)
data['Embarked'].value_counts()
embarked_categories = ['S','C','Q']
data['Embarked'] = pd.Categorical(data['Embarked'],embarked_categories,ordered = True)
median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)
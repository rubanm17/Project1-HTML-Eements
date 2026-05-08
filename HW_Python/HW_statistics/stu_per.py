import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('StudentsPerformance.csv')
data.head(5)
data.isnull().sum()
data.dtypes

math = data['math score'].mean()
print("The average marks scored on math is: ",math)
reading = data['reading score'].mean()
print("The average marks scored on reading is: ",reading)
writing = data['writing score'].mean()
print("The average marks scored on writing is: ",writing)

gender_category = ['Male','Female']
data['Gender'] = pd.Categorical(data['Gender'],gender_category,ordered = True)
sns.countplot(x='Gender',data=data)
plt.show()

race_ethinicity_categories = ['group A','group B','group C','group D','group E']
data['race/ethinicity'] = pd.categorical(data['ethinicity'],race_ethinicity_categories,ordered = True)
sns.countplot(x='race/ethinicity',data=data)
plt.show()

parental_lvl_edu_category = ["master's degree","bachelor's degree","some college","associate's degree","high school","some high school"]
data['parental level of education'] = pd.Categorical(data['parental level of education'],parental_lvl_edu_category,ordered = True)
sns.countplot(x='parental level of education',data=data)
plt.show()

lnc_cat = ['standard lunch','free/reduced lunch']
data['lunch'] = pd.Categorical(data['lunch'],lnc_cat,ordered = True)
sns.countplot(x='lunch',data=data)
plt.show()

test_preparation_course_cat = ['none','completed']
data['test preparation course'] = pd.Categorical(data['test preparation course'],test_preparation_course_cat,ordered = True)
sns.countplot(x='test preparation course',data=data)
plt.show()

plt.pie(data['race/ethinicity'].value_counts(), labels=data['race/ethinicity'].value_counts().index, data=data)
plt.show()

plt.pie(data['parental level of education'].value_counts(), labels=data['parental level of education'].value_counts().index, data=data)
plt.show()

print("skewness of race/ethinicity:", data['race/ethinicity'].skew())
print("skewness of parental level of education:", data['parental level of education'].skew())

sns.heatmap(data.corr(numeric_only=True), annot=True)
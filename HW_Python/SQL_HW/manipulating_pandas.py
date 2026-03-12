import pandas as pd

# 1. Create dictionary
data = {
    "Id": [1,2,3,4],
    "Name": ["Pankaj","Meghna","David","Lisa"],
    "Role": ["CEO", None, None, None],
    "Salary": [100,200,None,None]
}

# 2. Create DataFrame
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 3. Print first 2 and last 2 rows
print("\nFirst 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

# 4. Total number of null values
print("\nTotal Null Values:")
print(df.isnull().sum().sum())

# 5. Detailed information
print("\nDataFrame Info:")
print(df.info())

# 6. Drop rows with null values
df_rows = df.dropna()
print("\nAfter Dropping Rows with Null Values:")
print(df_rows)

# 7. Drop columns with null values
df_cols = df.dropna(axis=1)
print("\nAfter Dropping Columns with Null Values:")
print(df_cols)

# 8. Fill Salary null values with 300
df_salary = df.copy()
df_salary["Salary"].fillna(300, inplace=True)
print("\nSalary Null Filled with 300:")
print(df_salary)

# 9. Fill Role null values with CEO
df_role = df.copy()
df_role["Role"].fillna("CEO", inplace=True)
print("\nRole Null Filled with CEO:")
print(df_role)
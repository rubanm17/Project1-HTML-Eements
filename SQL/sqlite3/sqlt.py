import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened database successfully")

import pandas as pd
tables = pd.read_sql("""SELECT
                     name FROM sqlite_master
                     WHERE type='table';""", conn)
print(tables)

matches = pd.read_sql("""SELECT * 
                      FROM Matches;""", conn)

matches.info()
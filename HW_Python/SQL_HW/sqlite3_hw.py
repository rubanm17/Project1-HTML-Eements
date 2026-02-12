import sqlite3

database = 'database.sqlite'

conmop = sqlite3.connect(database)
print("Pro mood ON!")

import pandas as pa
tables = pa.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE TYPE = 'table';""", conmop)
print(tables)
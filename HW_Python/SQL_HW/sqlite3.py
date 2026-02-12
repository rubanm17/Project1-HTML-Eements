import sqlite3

database23 = 'database23' \
'.sqlite'

connect = sqlite3.connect(database23)
print("Pro mood ON!")

import pandas as pa
tables = pa.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE TYPE = 'table';""", connect)
print(tables)
import pandas as pd
import sqlite3

database = "match.sqlite"
conn = sqlite3.connect(database)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in the database:\n", tables)

match_details = pd.read_sql_query("""SELECT m.Season_Id, m.Match_Id, v.Venue_Name, c.City_Name,t.Team_Name AS Winner FROM Match AS m 
 INNER JOIN venue AS v ON m.Venue_Id = v.Venue_Id
 INNER JOIN city AS c ON v.City_Id = c.City_Id
 INNER JOIN team AS t ON m.Winner_Id = t.Team_Id;
                                  """, conn) 
print("Match Details:\n", match_details)

conn.close()
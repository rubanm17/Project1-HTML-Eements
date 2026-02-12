import sqlite3
import pandas as pd

database = 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened database successfully")

tables = pd.read_sql("""SELECT
                     name FROM sqlite_master
                        WHERE type='table';""", conn)
print("\n All tables in the database:")
print(tables)

teams = pd.read_sql("""SELECT * 
                      FROM Team;""", conn)
print("\nTeams:")
print(teams.head())

matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)
print("\nMatches:")
print(matches.head())

MI_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_winner = 7;""", conn)
print("\nMatches mumbai indians wins:")
print(MI_wins.head())

MI_58_59 = pd.read_sql("""SELECT * FROM Match WHERE (Match_winner = 7) AND Season_Id IN (8,9);""", conn)
print("\nMatches mumbai indians wins in season 8 and 9:")
print(MI_58_59.head())

new_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'De%';""", conn)
print("\nTeams starting with De:")
print(new_teams)

min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin) AS MinMargin, MAX(Win_Margin) AS MaxMargin FROM Match;""", conn)
print("\nMinimum and Maximum Win Margin:")
print(min_max_margin)

conn.close()
print("\nConnection closed.")
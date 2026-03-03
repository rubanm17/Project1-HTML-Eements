import pandas as pd
import sqlite3
database = "match_2.sqlite"
conn = sqlite3.connect(database)

table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(table)

print("All data from match table")

season = pd.read_sql_query("SELECT * FROM Season;", conn)
print("Season:\n",season)
CSK_Wins = pd.read_sql_query("SELECT * FROM Match WHERE Match_Winner = 3 AND Season_Id = 1;", conn)
print("CSK Wins in 2015:\n", CSK_Wins)
match_runs = pd.read_sql_query("SELECT Match_Id,runs_scored,Innings_No FROM Batsman_Scored WHERE Batsman_Id = 1 AND Match_Id IN (SELECT Match_Id FROM Match WHERE Season_Id = 1);", conn)
print("Matches with runs scored greater than 5 in 2015:\n",match_runs)
avg_runs = pd.read_sql_query("""SELECT Match_Id,Runs_scored,Innings_No
                       FROM Batsman_Scored
                       WHERE Innings_No = 1 AND Runs_scored > (SELECT AVG(Runs_scored) FROM Batsman_Scored);""", conn)
print("Matches with scored runs greater than average :\n", avg_runs)

conn.close()
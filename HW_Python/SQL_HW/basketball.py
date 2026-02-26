import sqlite3
import pandas as pd

# Connect to database (creates file if not exists)
conn = sqlite3.connect("basketball.db")
cursor = conn.cursor()

print("Database Connected Successfully!")

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Team (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT,
    team_name TEXT,
    position TEXT,
    points INTEGER
);
""")

# --------- INPUT SECTION ----------
n = int(input("Enter number of players: "))

for i in range(n):
    print(f"\nEnter details for Player {i+1}")
    name = input("Player Name: ")
    team = input("Team Name: ")
    position = input("Position (Guard/Forward/Center): ")
    points = int(input("Points Scored: "))

    cursor.execute("""
    INSERT INTO Team (player_name, team_name, position, points)
    VALUES (?, ?, ?, ?);
    """, (name, team, position, points))

conn.commit()
print("\nData Inserted Successfully!")

# --------- DISPLAY SECTION ----------

# 1️⃣ Show all players
df = pd.read_sql("SELECT * FROM Team;", conn)
print("\nAll Players:")
print(df)

# 2️⃣ Highest Scorer
highest = pd.read_sql("""
SELECT * FROM Team
WHERE points = (SELECT MAX(points) FROM Team);
""", conn)
print("\nHighest Scorer:")
print(highest)

# 3️⃣ Average Points Per Team
avg_points = pd.read_sql("""
SELECT team_name, AVG(points) as Avg_Points
FROM Team
GROUP BY team_name;
""", conn)
print("\nAverage Points Per Team:")
print(avg_points)

conn.close()
import sqlite3

conn = sqlite3.connect("basketball.sqlite")

# 1. Show tables
print("\nAll Tables:")
for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)

# 2. Team table structure
print("\nTeam Table Columns:")
for row in conn.execute("PRAGMA table_info(Team);"):
    print(row)

# 3. Team_Attributes structure
print("\nTeam_Attributes Columns:")
for row in conn.execute("PRAGMA table_info(Team_Attributes);"):
    print(row)

# 4. Subquery for New York teams
print("\nNew York Teams Attributes:")
query = """
SELECT *
FROM Team_Attributes
WHERE team_api_id IN (
    SELECT team_api_id
    FROM Team
    WHERE team_long_name LIKE '%New York%'
);
"""
query1 = conn.execute(query);
print(query1)
for row in conn.execute(query):
    print(row)

conn.close()
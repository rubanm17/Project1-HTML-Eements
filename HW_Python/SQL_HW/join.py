import sqlite3

conn = sqlite3.connect("school.db")

print("\nINNER JOIN:")
for row in conn.execute("""
SELECT C_S.Name, MARKS.Subject, MARKS.Marks
FROM C_S
INNER JOIN MARKS
ON C_S.Roll_NO = MARKS.Roll_NO
"""):
    print(row)

print("\nLEFT OUTER JOIN:")
for row in conn.execute("""
SELECT C_S.Name, MARKS.Subject, MARKS.Marks
FROM C_S
LEFT JOIN MARKS
ON C_S.Roll_NO = MARKS.Roll_NO
"""):
    print(row)

print("\nCROSS JOIN:")
for row in conn.execute("""
SELECT C_S.Name, MARKS.Subject
FROM C_S
CROSS JOIN MARKS
LIMIT 5
"""):
    print(row)

print("\nUNION:")
for row in conn.execute("""
SELECT Name FROM C_S
UNION
SELECT Subject FROM MARKS
"""):
    print(row)

conn.close()

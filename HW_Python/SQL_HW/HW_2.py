import sqlite3

conn = sqlite3.connect("school.db")

conn.execute("""
CREATE TABLE students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    marks INTEGER,
    city TEXT
)
""")
conn.commit()    

print("ALL STUDENTS:")
for row in conn.execute("SELECT * FROM students"):
    print(row)

print("\nSTUDENTS FROM DELHI:")
for row in conn.execute("SELECT name, marks FROM students WHERE city = 'Delhi'"):
    print(row)

print("\nSTUDENTS WHOSE NAME STARTS WITH 'An':")
for row in conn.execute("SELECT name FROM students WHERE name LIKE 'An%'"):
    print(row[0])

min_marks = conn.execute(
    "SELECT MIN(marks) FROM students"
).fetchone()[0]
print("\nMINIMUM MARKS:", min_marks)

max_marks = conn.execute(
    "SELECT MAX(marks) FROM students"
).fetchone()[0]
print("MAXIMUM MARKS:", max_marks)

conn.close()

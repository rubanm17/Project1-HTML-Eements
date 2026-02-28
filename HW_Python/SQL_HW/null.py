import sqlite3

conn = sqlite3.connect("database.db")

print("ALL RECORDS IN C_S TABLE:")
for row in conn.execute("SELECT * FROM C_S"):
    print(row)

print("\nPRIMARY KEY CONSTRAINT DEMO:")

try:
    conn.execute("""
    INSERT INTO C_S (SNO, Roll_NO, Name, GENDER, Email_ID, Contact_No)
    VALUES (1, 106, 'Duplicate', 'Male', 'dup@gmail.com', 9000000000)
    """)
    conn.commit()
except Exception as e:
    print("Error:", e)

print("\nNOT NULL CONSTRAINT DEMO:")

try:
    conn.execute("""
    INSERT INTO C_S (SNO, Roll_NO, Name, GENDER, Email_ID, Contact_No)
    VALUES (6, 106, NULL, 'Male', 'null@gmail.com', 9111111111)
    """)
    conn.commit()
except Exception as e:
    print("Error:", e)

print("\nDEFAULT CONSTRAINT DEMO:")

conn.execute("""
INSERT INTO C_S (SNO, Roll_NO, Name, GENDER, Email_ID, Contact_No)
VALUES (6, 106, 'Ravi', 'Male', 'ravi@gmail.com', 9333333333)
""")
conn.commit()

for row in conn.execute("SELECT Name, AGE FROM C_S WHERE SNO = 6"):
    print(row)

print("\nNULL VALUE CHECK:")

try:
    conn.execute("""
    INSERT INTO C_S (SNO, Roll_NO, Name, AGE, GENDER, Email_ID, Contact_No)
    VALUES (7, 107, 'Kiran', NULL, 'Male', 'kiran@gmail.com', 9444444444)
    """)
    conn.commit()

    print("NULL accepted for AGE")
except Exception as e:
    print("Error:", e)

print("\nFINAL TABLE DATA:")
for row in conn.execute("SELECT * FROM C_S"):
    print(row)

conn.close()

import sqlite3

# Create users table
conn = sqlite3.connect("../school.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS details (
        Roll_no INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Marks TEXT NOT NULL
    )
""")
conn.commit()
conn.close()

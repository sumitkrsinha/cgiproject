#!/usr/bin/env python
import cgi
import sqlite3

print("Content-Type: text/html\r\n\r\n")

# Connect to SQLite database
conn = sqlite3.connect("./school.db")
cur = conn.cursor()

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Insert new user into the database
query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
try:
    cur.execute(query)
    conn.commit()
    print("<p>Registration successful. You can now <a href='login.html'>login</a>.</p>")
except Exception as e:
    print(f"<p>Registration failed. Error: {e}</p>")

# Close database connection
conn.close()

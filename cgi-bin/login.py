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

# Validate login credentials
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
cur.execute(query)
user = cur.fetchone()

if user:
    html = f'''
       <html>
       <body>
       <script>
       document.cookie = "username={username}";
       window.location.href = '/dashboard.html';
       </script>
       </body>
       </html>'''
    print(html)
else:
    query1 = f"SELECT * FROM users WHERE username='{username}'"
    cur.execute(query1)
    registered = cur.fetchone()
    if registered:
        print(f"Login failed. Invalid credentials.\r\n")
    else:
        print(f"Login failed. User Does Not Exist.\r\n")


# Close database connection
conn.close()

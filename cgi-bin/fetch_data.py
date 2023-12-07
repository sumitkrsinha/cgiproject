#!/usr/bin/env python3
import sqlite3
import json

# Enable CORS (Cross-Origin Resource Sharing)
print("Content-type: application/json")
print("Access-Control-Allow-Origin: *")
print()

# Connect to SQLite database
conn = sqlite3.connect("./school.db")
cursor = conn.cursor()

# Fetch data from the table
cursor.execute("SELECT * FROM details")
rows = cursor.fetchall()
# print(rows)

# Convert data to JSON format
data = [{"Roll_no": row[0], "Name": row[1], "Marks": row[2]} for row in rows]
# print(data)

# Print JSON response
print(json.dumps(data, indent=2))

# Close database connection
conn.close()

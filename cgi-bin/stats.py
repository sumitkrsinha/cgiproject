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
cursor.execute("SELECT * FROM details WHERE Marks = ( SELECT max(Marks) FROM details);")
rows = cursor.fetchall()

# Calculate average marks and total entries
cursor.execute("SELECT AVG(Marks), COUNT(*) FROM details")
stats = cursor.fetchone()

# Convert data to JSON format
data = {
    "highestScorer": [{"Roll_no": row[0], "Name": row[1], "Marks": row[2]} for row in rows],
    "averageMarks": stats[0],
    "totalEntries": stats[1]
}
# print(data.Roll_no)
# Print JSON response
print(json.dumps(data, indent=2))



# Close database connection
conn.close()

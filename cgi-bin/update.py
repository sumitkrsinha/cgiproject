import sqlite3, cgi

print("Content-Type:text/html\r\n\r\n")

conn = sqlite3.connect("./school.db")
cur = conn.cursor()

form = cgi.FieldStorage()
roll_no = form.getvalue("rno")
name = form.getvalue("name")
marks = form.getvalue("marks")
# print(rno, name, dept)

query = "update details SET Name='" +name+ "', Marks='" +marks+ "' where Roll_no=" +roll_no
# print(typeof(roll_no))

try:
    rs = cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("updated successfully")
    html = f'''
           <html>
           <body>
           <script>
           window.location.href = '/dashboard.html';
           </script>
           </body>
           </html>'''
    print(html)
conn.close()
# cur.close()


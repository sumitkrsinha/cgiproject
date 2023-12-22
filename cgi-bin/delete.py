import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("./school.db")
cur=conn.cursor()

form=cgi.FieldStorage()
roll_no = form.getvalue("rollno")
query="delete from details where Roll_no="+roll_no

try:
    cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("deleted successfully")
    html = f'''
           <html>
           <body>
           <script>
           window.location.href = '/dashboard.html';
           </script>
           </body>
           </html>'''
    print(html)
finally:
    conn.close()
    #cur.close()

import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("./school.db")
cur=conn.cursor()

form=cgi.FieldStorage()
roll_no = form.getvalue("rno")
name = form.getvalue("name")
marks = form.getvalue("marks")
#print(rno,name,dept)

sql="insert into details values('"+roll_no+"','"+name+"','"+marks+"')"
#print(sql)

try:
    rs=cur.execute(sql)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("successfully inserted")
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
cur.close()
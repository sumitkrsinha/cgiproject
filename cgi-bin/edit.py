import sqlite3, cgi

print("Content-Type:text/html\r\n\r\n")
conn = sqlite3.connect("./school.db")
cur = conn.cursor()
form = cgi.FieldStorage()
roll_no = form.getvalue("rno")
query = "select * from details where Roll_no=" + str(roll_no)
try:
    cur.execute(query)
    # record = cur
    # print(record)
except Exception as e:
    print(e)
else:

    for record in cur:
        pass
    html = f'''
    <html>
    <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="../styles.css">
    </head>
    <body class="bg-dark">
    <div class="container form-cont bg-light p-5">
    <div class="first">
    <h3>Edit Values</h3>
    <div class="links">
    <a href="../add.html">Add</a>
    <a href="../delete.html">Delete</a>
    <a href="../dashboard.html">D.board</a>
    </div>
    </div>
    <form action="update.py" method="PUT">
    <input type="number" class="form-control" value="{(record[0])}" name="rno" readonly><br/>
    <input type="text" class="form-control" value="{(record[1])}" name="name"><br/>
    <input type="number" class="form-control" value="{record[2]}" name="marks"><br/>
    <input type="submit" class="btn btn-primary" value="Update" >
    </form>
    </div>
    </body>
    </html>'''
    print(html)
finally:
    conn.close()
# cur.close()

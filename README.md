# cgiproject

##### This is a POC project for CRUD operations on school database.

### Technologies used:
- JavaScript
- CSS
- Html
- Bootstrap
- Python CGI
- SQLite Database
- Apache web server

#### Screenshots

![Alt text](./images/registration.jpg)


![Alt text](./images/Login.jpg)


![Alt text](./images/dashboard.jpg)


![Alt text](./images/add.jpg)


![Alt text](./images/edit.jpg)


![Alt text](./images/delete.jpg)


## How to run the Project

- Locate the terminal to "cgi-bin" directory and the run "python create_table.py" to initialize the database and for table creation.
- Set permission so that CGI scripts have executable permission. Run the following commands:

      #### chmod +x cgi-bin/registration.py
      #### chmod +x cgi-bin/login.py
      #### chmod +x cgi-bin/insert.py
      #### chmod +x cgi-bin/delete.py
      #### chmod +x cgi-bin/edit.py
      #### chmod +x cgi-bin/fetch_data.py
      #### chmod +x cgi-bin/update.py

- Run web server to run CGI scripts using "python -m http.server 8000 --cgi"
- Access website at localhost:8000




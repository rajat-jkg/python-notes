# to connect a python application with mysql server we need to insatll two python packages with pip
# 1. mysql-connector-python
# 2. mysql

import mysql.connector # importing package


mydb = mysql.connector.connect(user = "root",passwd = "rajat", host = "localhost")
# setting connection with database
# syntax: variable = mysql.connector.connect(user = "username",passwd = "password", host = "hstname or IP adress of server", database= "database name")
# Note: giveng database name as argument is optional


cur = mydb.cursor() # initalising cursor
# cursor can be used to execute sql queries
# Syntax: cursor_name = cursor.execute("SQL query")
# A cursor when excutes a query stores the output of that query in itself in form of a sequence of tupples.
# That output can be extracted through a for loop 


#Example
cur.execute("use demo")
cur.execute("Select PersonID, FirstName, LastName from Persons")
print('id \t Name')
for i in cur:
    print(i[0],"\t",i[1],i[2])
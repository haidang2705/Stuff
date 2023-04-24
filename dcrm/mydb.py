import mysql.connector;

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'haidang2000',
)
# prepare a cursor object 
# The MySQLCursor of mysql-connector-python (and similar libraries) is used to execute statements to communicate with the MySQL database.

# Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.
cursorObject = dataBase.cursor();

#create a database
cursorObject.execute("CREATE DATABASE dcrm");
print("All Done!!!!");


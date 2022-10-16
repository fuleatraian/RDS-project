import mysql.connector

#Connect to MariaDB via .connect method and user the root user 
Module2 = mysql.connector.connect(user = 'root')
print(Module2)

mycursor = Module2.cursor()


mycursor.execute("DROP DATABASE IF EXISTS salesdb;")
mycursor.execute("CREATE DATABASE IF NOT EXISTS salesdb;")
mycursor.execute("SHOW DATABASES;")

# Display the available databases

print("Databases:")
for x in mycursor:
    print(x)


#Use the salesDB database
mycursor.execute("USE salesdb;")

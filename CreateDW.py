import mysql.connector

# Connect to MariaDB via the .connector method and create the data warehouse 
Module2 = mysql.connector.connect(user = 'root')
mycursor = Module2.cursor()

# Now create the data warehouse
mycursor.execute('DROP DATABASE IF EXISTS sales_olap;')
mycursor.execute('CREATE DATABASE IF NOT EXISTS sales_olap;')
mycursor.execute('SHOW DATABASES;')


# Display the available databases

print("Databases:")
for x in mycursor:
    print(x)


#Use the sales_OLAP database
mycursor.execute("USE sales_olap;")
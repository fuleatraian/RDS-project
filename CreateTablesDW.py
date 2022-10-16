import mysql.connector

# Connect to the database, more specifically, to the data warehouse
dw = mysql.connector.connect(user = 'root', database = 'sales_olap')
mycursor = dw.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS employee
                        (   
                            emp_id int(5) PRIMARY KEY,
                            employee_full_name varchar(30),
                            gender ENUM('M', 'F'),
                            age int(2),
                            hire_date DATE,
                            team_id int(5),
                            supervisor_full_name varchar(30),
                            dept_name varchar(15),
                            managers varchar(30)
                        )
                """
                )


mycursor.execute("""CREATE TABLE IF NOT EXISTS location
                        (
                            loc_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            country_name varchar(20),
                            city_name varchar(20),
                            area_postcode varchar(7)
                        )
                """
                )


mycursor.execute("""CREATE TABLE IF NOT EXISTS property
                        (
                            prop_id int(5) PRIMARY KEY,
                            type_name varchar(10),
                            no_bed int(2),
                            no_bath int(2),
                            price int(10),
                            status_name varchar(10)
                        )
                """
                )


mycursor.execute("""CREATE TABLE IF NOT EXISTS customer
                        (
                            custom_id int(5) PRIMARY KEY,
                            first_name varchar(20),
                            second_name varchar(20),
                            budget int(10),
                            intention ENUM('BUY', 'SELL', 'RENT')
                        )
                """
                )


mycursor.execute("""CREATE TABLE IF NOT EXISTS agreement
                        (
                            agree_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            custom_id int(5),
                            prop_id int(5),
                            loc_id int(5),
                            emp_id int(5),
                            tax_value int(5),
                            total_price int(11),
                            FOREIGN KEY (custom_id) REFERENCES customer (custom_id) ON UPDATE CASCADE,
                            FOREIGN KEY (prop_id) REFERENCES property (prop_id) ON UPDATE CASCADE,
                            FOREIGN KEY (loc_id) REFERENCES location (loc_id) ON UPDATE CASCADE,
                            FOREIGN KEY (emp_id) REFERENCES employee (emp_id) ON UPDATE CASCADE
                        )
                """
                )
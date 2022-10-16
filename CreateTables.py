
#Create the tables

# from mycursor to connect to the database
import mysql.connector
db = mysql.connector.connect(user = 'root',
  database="salesdb"
)


mycursor = db.cursor()


mycursor.execute("""CREATE TABLE IF NOT EXISTS country 
                            (
                                country_id int(5) AUTO_INCREMENT PRIMARY KEY, 
                                country_name varchar(25) NOT NULL
                            );
                """
                )


mycursor.execute("""CREATE TABLE IF NOT EXISTS city 
                        (
                            city_id int(5) AUTO_INCREMENT PRIMARY KEY, 
                            city_name varchar(25) NOT NULL,
                            country_id int(5),
                            CONSTRAINT FOREIGN KEY (country_id)
                            REFERENCES country (country_id) 
                        );
                """
                )


mycursor.execute("""CREATE TABLE IF NOT EXISTS area
                        (
                            area_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            area_postcode varchar(7) UNIQUE KEY NOT NULL,
                            city_id int(5),
                            CONSTRAINT fk_area FOREIGN KEY (city_id)
                            references city (city_id)
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS department
                        (
                            dept_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            dept_name varchar(10) NOT NULL,
                            city_id int(5),
                            CONSTRAINT fk_dept FOREIGN KEY (city_id)
                            REFERENCES city (city_id) ON DELETE CASCADE
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS employees
                        (
                            dept_id int(5),
                            emp_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            first_name varchar(10) NOT NULL,
                            second_name varchar(10) NOT NULL,
                            gender ENUM('M', 'F'),
                            age int(2),
                            hire_date DATE NOT NULL,
                            CONSTRAINT fk_employees FOREIGN KEY (dept_id)
                            REFERENCES department (dept_id) ON DELETE CASCADE
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS sales_supervisor
                        (
                            emp_id int(5),
                            experience int(2),
                            CONSTRAINT pk_sup PRIMARY KEY (emp_id),
                            CONSTRAINT fk_sup FOREIGN KEY (emp_id)
                            REFERENCES employees (emp_id) ON DELETE CASCADE
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS team
                        (
                            emp_id int(5),
                            team_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            CONSTRAINT fk_team FOREIGN KEY (emp_id)
                            REFERENCES sales_supervisor (emp_id) ON DELETE CASCADE
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS sales_rep
                        (
                            emp_id int(5),
                            team_id int(5),
                            active_negot int(5),
                            specialization ENUM('SELL', 'BUY'),
                            CONSTRAINT pk_sales_rep PRIMARY KEY (emp_id),
                            CONSTRAINT fk1_sales_rep FOREIGN KEY (emp_id)
                            REFERENCES employees (emp_id) ON DELETE CASCADE,
                            CONSTRAINT fk2_sales_rep FOREIGN KEY (team_id)
                            REFERENCES team (team_id) ON DELETE CASCADE
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS report_dept
                        (
                            rep_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            rep_name varchar(20) NOT NULL
                        );
                """)



mycursor.execute("""CREATE TABLE IF NOT EXISTS sales_chief
                        (
                            emp_id int(5),
                            area_id int(5),
                            rep_id int(5),
                            performance varchar(20),
                            target varchar(20),
                            PRIMARY KEY (emp_id, area_id),
                            FOREIGN KEY (emp_id) REFERENCES employees (emp_id) ON DELETE CASCADE,
                            FOREIGN KEY (area_id) REFERENCES area (area_id) ON DELETE CASCADE,
                            FOREIGN KEY (rep_id) REFERENCES report_dept (rep_id) ON DELETE CASCADE
                        );
                """)

mycursor.execute("""CREATE TABLE IF NOT EXISTS customer
                        (
                        custom_id int(5) AUTO_INCREMENT PRIMARY KEY,
                        first_name varchar(10),
                        last_name varchar(10),
                        budget int(10),
                        intention ENUM('BUY', 'SELL', 'RENT'),
                        emp_id int(5),
                        CONSTRAINT fk_customer FOREIGN KEY (emp_id)
                        REFERENCES sales_rep (emp_id) 
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS property_type
                        (
                            type_id int(1) AUTO_INCREMENT PRIMARY KEY,
                            type_name varchar(10),
                            UNIQUE KEY (type_name)
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS property_status
                        (
                            status_id int(1) AUTO_INCREMENT PRIMARY KEY,
                            status_name varchar(10),
                            UNIQUE KEY (status_name)
                        );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS property
                        (
                            prop_id int(5) AUTO_INCREMENT PRIMARY KEY,
                            area_id int(5),
                            type_id int(1),
                            no_bed int(2),
                            no_bath int(2),
                            price int(10),
                            status_id int(1),
                            emp_id int(5),
                            FOREIGN KEY (area_id) REFERENCES area (area_id) ON DELETE CASCADE,
                            FOREIGN KEY (type_id) REFERENCES property_type (type_id) ON DELETE CASCADE,
                            FOREIGN KEY (status_id) REFERENCES property_status (status_id) ON DELETE CASCADE,
                            FOREIGN KEY (emp_id) REFERENCES sales_rep (emp_id) ON DELETE CASCADE
                        );
                """)
import CreateTables
import Functions
import random
from datetime import date

# Insert data into country table
country_sql = """INSERT INTO country (country_name) VALUES (%s);"""
country_val = [('USA',), ('Spain',), ('UK',)]
CreateTables.mycursor.executemany(country_sql, country_val)


# Insert data into city table
city_sql = """INSERT INTO city (city_name, country_id) VALUES (%s, %s);"""
city_val = [('New York', 1), ('Miami', 1), ('San Francisco', 1), ('Barcelona', 2), ('Madrid', 2), ('London', 3), ('Manchester', 3), ('Liverpool', 3)]
CreateTables.mycursor.executemany(city_sql, city_val)


# Insert data into area table
area_sql = """INSERT INTO area (area_postcode, city_id) VALUES (%s, %s);"""
area_val = Functions.area_generator(8)
CreateTables.mycursor.executemany(area_sql, area_val)


# Insert data into department table
dept_sql = """INSERT INTO department (dept_name, city_id) VALUES (%s, %s);"""
dept_val = [('Sales', 7), ('Marketing', 5), ('Sales', 2), ('Marketing', 2), ('Sales', 8)]
CreateTables.mycursor.executemany(dept_sql, dept_val)


# Insert data into employee table
emp_sql = """INSERT INTO employees (dept_id, first_name, second_name, gender, age, hire_date) VALUES (%s, %s, %s, %s, %s, %s);"""
# emp_val = [(1, 'Sia', 'Villanueva', 'F', random.randint(30, 40), date(year = 2020, month = 4, day = 23)),
#             (1, 'Agnes', 'Rice', 'F', random.randint(30, 40), date(year = 2019, month = 3, day = 12)),
#             (3, 'James', 'Bray', 'M', random.randint(30, 40), date(year = 2014, month = 5, day = 30)),
#             (3, 'Matteo', 'Kim', 'M', random.randint(30, 40), date(year = 2018, month = 3, day = 21)),
#             (1, 'Catriona', 'Cherry', 'F', random.randint(30, 40), date(year = 2015, month = 7, day = 24)),
#             (5, 'Finn', 'Summers', 'M', random.randint(30, 40), date(year = 2021, month = 8, day = 24)),
#             (5, 'Asif', 'Stevenson', 'M', random.randint(30, 40), date(year = 2021, month = 5, day = 16)),
#             (5, 'Eshaal', 'Lozano', 'M', random.randint(30, 40), date(year = 2015, month = 7, day = 8)),
#             (3, 'Billy', 'Hamilton', 'M', random.randint(30, 40), date(year = 2021, month = 3, day = 19)),
#             (3, 'Maizie', 'Orozco', 'F', random.randint(30, 40), date(year = 2018, month = 2, day = 20)),
#             (1, 'Mina', 'Reyes', 'F', random.randint(30, 40), date(year = 2018, month = 7, day = 28))
#             ]
emp_val = Functions.employee_generator(22)
CreateTables.mycursor.executemany(emp_sql, emp_val)


# Insert data into report_dept table
report_dept_sql = """INSERT INTO report_dept (rep_name) VALUES (%s);"""
report_dept_val = [('Customer Support',), ('Quality',)]
CreateTables.mycursor.executemany(report_dept_sql, report_dept_val)


# Insert data into sales_chief table
chief_sql = """INSERT INTO sales_chief (emp_id, performance, target, area_id, rep_id) VALUES (%s, %s, %s, %s, %s);"""
# chief_val = [(1, 1.5, 2.5, 4, 2),
#             (8, 2.7, 4.6, 7, 2), 
#             (9, 0.3, 1.8, 3, 1),
#             (13, 1.2, 1.8, 4, 2),
#             (15, 0.9, 2.9, 7, 2), 
#             (18, 0.7, 4.1, 3, 1),
#             (20, 2.4, 4.5, 3, 1)
#             ]
chief_val = Functions.chief_generator(7)
CreateTables.mycursor.executemany(chief_sql, chief_val)


# Insert data into sales_supervisor table
supervisor_sql = """INSERT INTO sales_supervisor (emp_id, experience) VALUES (%s, %s);"""
supervisor_val = [(1, 10), (2, 8), 
                  (3, 5), (4, 15)
                 ]
CreateTables.mycursor.executemany(supervisor_sql, supervisor_val)


# Insert data into team table
team_sql = """INSERT INTO team (emp_id) VALUES (%s);"""
team_val = [(1,), (2,), (3,), (4,)]
CreateTables.mycursor.executemany(team_sql, team_val)


# Insert data into sales_rep table
rep_sql = """INSERT INTO sales_rep (emp_id, team_id, active_negot, specialization) VALUES (%s, %s, %s, %s)"""
rep_val = [(12, 1, 8, 'SELL'), (13, 1, 3, 'BUY'), (14, 3, 10, 'BUY'), 
           (15, 3, 6, 'BUY'), (16, 3, 15, 'SELL'), (17, 4, 15, 'SELL'),
           (18, 2, 6, 'BUY'), (19, 2, 15, 'SELL'), (20, 4, 15, 'SELL'),
           (21, 3, 6, 'BUY'), (22, 2, 15, 'SELL')
           ]
CreateTables.mycursor.executemany(rep_sql, rep_val)


# Insert data into property_type table
proptype_sql = """INSERT INTO property_type (type_name) VALUES (%s);"""
proptype_val = [('House',), ('Flat/Apartment',), ('Bungalow',), ('Land',), ('Comercial Property',)]
CreateTables.mycursor.executemany(proptype_sql, proptype_val)


# Insert data into property_status table
propstatus_sql = """INSERT INTO property_status (status_name) VALUES (%s);"""
propstatus_val = [('TO BUY',), ('TO LET',), ('LET AGREED',), ('SOLD',)]
CreateTables.mycursor.executemany(propstatus_sql, propstatus_val)


# Insert data into property table
prop_sql = """INSERT INTO property (area_id, type_id, no_bed, no_bath, price, status_id, emp_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
prop_val = Functions.property_generation(1000)
CreateTables.mycursor.executemany(prop_sql, prop_val)


# Insert data into the customer table
customer_sql = """INSERT INTO customer (first_name, last_name, budget, intention, emp_id) VALUES (%s, %s, %s, %s, %s)"""
customer_val = Functions.customer_generator(200)
CreateTables.mycursor.executemany(customer_sql, customer_val)



CreateTables.db.commit()









import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:''@localhost/salesdb')
conn = engine.connect()


"""Answering and returning the queries using SQL but display them in a pandas dataframe"""


#First, we want to establish the connection of this python file to the database
# db = mysql.connector.connect(user = 'root', database='salesdb')


# Display names of representatives, details of the properties they represent, and names of their supervisors

df1 = pd.read_sql("""Select emp.first_name AS 'First Name', emp.second_name AS 'Last name', sup.first_name AS 'Supervisor First Name', 
                    sup.second_name AS 'Supervisor Last name', prop.prop_id, prop.area_id, prop.type_id, prop.no_bed, prop.no_bath, 
                    prop.price, prop.status_id FROM 
                        employees emp INNER JOIN sales_rep rep ON emp.emp_id = rep.emp_id
                                      INNER JOIN property prop ON emp.emp_id = prop.emp_id
                                      LEFT JOIN team ON rep.team_id = team.team_id
                                      LEFT JOIN (SELECT emp.emp_id, emp.first_name, emp.second_name 
                                                 FROM sales_supervisor supervisor
                                                    INNER JOIN employees emp ON
                                                    supervisor.emp_id = emp.emp_id) sup
                                        ON team.emp_id = sup.emp_id
                    ;
                                      
                """, con = conn)


print(df1.head())



# Display details of customers together with details of their areas and names of the managers of their areas


df2 = pd.read_sql("""SELECT cust.custom_id, cust.first_name AS 'First Name', cust.last_name AS 'Second Name',
                        cust.budget, cust.intention, area.area_postcode, area.city_id,
                        chiefdata.first_name AS 'Manager First Name', chiefdata.second_name AS 'Manager Second Name'
                     FROM customer cust
                        LEFT JOIN sales_rep rep ON cust.emp_id = rep.emp_id
                        LEFT JOIN employees emp ON emp.emp_id = rep.emp_id
                        LEFT JOIN department dept ON emp.dept_id = dept.dept_id
                        LEFT JOIN city ON city.city_id = dept.city_id
                        LEFT JOIN area ON area.city_id = city.city_id
                        LEFT JOIN (SELECT emp.emp_id, emp.first_name, emp.second_name, chief.area_id
                                FROM employees emp
                                        INNER JOIN sales_chief chief ON chief.emp_id = emp.emp_id
                                    ) chiefdata
                            ON area.area_id = chiefdata.area_id;
                  """, con = conn)


print(df2.head())









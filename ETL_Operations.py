from sqlalchemy import create_engine
import pandas as pd
import numpy as np


engine_oltp = create_engine('mysql+pymysql://root:''@localhost/salesdb')
engine_olap = create_engine('mysql+pymysql://root:''@localhost/sales_olap')
conn_oltp = engine_oltp.connect()
conn_olap = engine_olap.connect()

emp_df = pd.read_sql("""
                        SELECT emp.emp_id, emp.first_name, emp.second_name, emp.gender, emp.age,
                                emp.hire_date, super.team_id, super.first_name AS sup_first_name, 
                                super.second_name AS sup_second_name, dept.dept_name, 
                                chief.first_name AS manager_first_name, chief.second_name AS manager_second_name
                            FROM employees emp
                                INNER JOIN sales_rep rep ON emp.emp_id = rep.emp_id
                                LEFT JOIN (SELECT team.team_id, sup.emp_id, emp.first_name, emp.second_name  
                                            FROM team
                                                LEFT JOIN sales_supervisor sup ON team.emp_id = sup.emp_id
                                                LEFT JOIN employees emp ON sup.emp_id = emp.emp_id
                                            ) super
                                        ON rep.team_id = super.team_id
                                LEFT JOIN department dept ON dept.dept_id = emp.dept_id
                                LEFT JOIN city ON dept.city_id = city.city_id
                                LEFT JOIN area ON city.city_id = area.city_id
                                LEFT JOIN (SELECT chief.area_id, emp.first_name, emp.second_name 
                                            FROM sales_chief chief
                                                INNER JOIN employees emp ON chief.emp_id = emp.emp_id) chief
                                        ON area.area_id = chief.area_id
                            WHERE emp.emp_id NOT IN (SELECT emp_id FROM sales_supervisor) 
                            AND emp.emp_id NOT IN (SELECT emp_id FROM sales_chief)

                        UNION

                        SELECT emp.emp_id, emp.first_name, emp.second_name, emp.gender, emp.age,
                                emp.hire_date, team.team_id, super.first_name AS sup_first_name, 
                                super.second_name AS sup_second_name, dept.dept_name, 
                                chief.first_name AS manager_first_name, chief.second_name AS manager_second_name
                            FROM employees emp
                                INNER JOIN sales_supervisor sup ON emp.emp_id = sup.emp_id
                                INNER JOIN team ON sup.emp_id = team.team_id
                                INNER JOIN (SELECT sup.emp_id, emp.first_name, emp.second_name  
                                            FROM team
                                                INNER JOIN sales_supervisor sup ON team.emp_id = sup.emp_id
                                                INNER JOIN employees emp ON sup.emp_id = emp.emp_id
                                            ) super
                                        ON super.emp_id = emp.emp_id
                                LEFT JOIN department dept ON dept.dept_id = emp.dept_id
                                LEFT JOIN city ON dept.city_id = city.city_id
                                LEFT JOIN area ON city.city_id = area.city_id
                                LEFT JOIN (SELECT chief.area_id, emp.first_name, emp.second_name 
                                            FROM sales_chief chief
                                                INNER JOIN employees emp ON chief.emp_id = emp.emp_id) chief
                                        ON area.area_id = chief.area_id 
                            WHERE emp.emp_id NOT IN (SELECT emp_id FROM sales_rep) 
                            AND emp.emp_id NOT IN (SELECT emp_id FROM sales_chief)
                            
                        UNION

                        SELECT emp.emp_id, emp.first_name, emp.second_name, emp.gender, emp.age,
                                emp.hire_date, 'Manager' AS team_id, super.first_name AS sup_first_name, 
                                super.second_name AS sup_second_name, dept.dept_name, 
                                chief.first_name AS manager_first_name, chief.second_name AS manager_second_name
                            FROM employees emp
                                INNER JOIN sales_chief manager ON emp.emp_id = manager.emp_id
                                LEFT JOIN (SELECT sup.emp_id, emp.first_name, emp.second_name  
                                            FROM team
                                                INNER JOIN sales_supervisor sup ON team.emp_id = sup.emp_id
                                                INNER JOIN employees emp ON sup.emp_id = emp.emp_id
                                            ) super
                                        ON super.emp_id = emp.emp_id
                                LEFT JOIN department dept ON dept.dept_id = emp.dept_id
                                LEFT JOIN city ON dept.city_id = city.city_id
                                LEFT JOIN area ON city.city_id = area.city_id
                                LEFT JOIN (SELECT chief.area_id, emp.first_name, emp.second_name 
                                            FROM sales_chief chief
                                                INNER JOIN employees emp ON chief.emp_id = emp.emp_id) chief
                                        ON area.area_id = chief.area_id 
                            WHERE emp.emp_id NOT IN (SELECT emp_id FROM sales_rep) 
                            AND emp.emp_id NOT IN (SELECT emp_id FROM sales_supervisor) 
                        ;

                    """, con = conn_oltp)


# The above query could also be written more elegantly as below. They produce similar results, the only difference being that it would be hard to notice the 
# sales supervisors and sales chiefs, because their teams 
#---------------------------------------------------------------------------------

# SELECT emp.emp_id, emp.first_name, emp.second_name, emp.gender, emp.age, emp.hire_date, team_sup.team_id,
# 		team_sup.first_name AS sup_first_name, team_sup.second_name AS sup_second_name, dept.dept_name,
#         manager.first_name AS chief_first_name, manager.second_name AS chief_second_name
# 	FROM employees emp
#     	LEFT JOIN department dept ON emp.dept_id = dept.dept_id
#         LEFT JOIN (SELECT city.city_id, emp.first_name, emp.second_name
#                    		FROM sales_chief chief
#                    			INNER JOIN employees emp ON chief.emp_id = emp.emp_id
#                    			RIGHT JOIN area ON area.area_id = chief.area_id
#                    			LEFT JOIN city ON city.city_id = area.city_id) manager
#         	ON dept.city_id = manager.city_id
#         LEFT JOIN (SELECT rep.emp_id, team.team_id, super.first_name, super.second_name 
#                    		FROM sales_rep rep
#                    			INNER JOIN team ON rep.team_id = team.team_id
#                    			LEFT JOIN (SELECT sup.emp_id, emp.first_name, emp.second_name
#                                        FROM sales_supervisor sup 
#                                        		INNER JOIN employees emp
#                                        			ON sup.emp_id = emp.emp_id) super
#                    			ON team.emp_id = super.emp_id) team_sup
#              ON emp.emp_id = team_sup.emp_id;

#--------------------------------------------------------------------------------------------



loc_df = pd.read_sql("""SELECT country.country_name, city.city_name, area.area_postcode FROM country
                            LEFT JOIN city ON country.country_id = city.country_id
                            LEFT JOIN area ON city.city_id = area.city_id
                        ;
                    """, con = conn_oltp)


prop_df = pd.read_sql("""SELECT prop.prop_id, pt.type_name, prop.no_bed, prop.no_bath, prop.price, ps.status_name
                            FROM property prop
                                INNER JOIN property_type pt ON pt.type_id = prop.type_id
                                INNER JOIN property_status ps ON ps.status_id = prop.status_id
                        ;
                    """, con = conn_oltp)


custom_df = pd.read_sql("""SELECT custom_id, first_name, last_name AS second_name, budget, intention
                                FROM customer;
                        """, con = conn_oltp)


agreement_df = pd.read_sql("""Select cust.custom_id, prop.prop_id, prop.area_id AS loc_id, prop.emp_id, 
                                0.05 * prop.price AS tax_value, 1.05 * prop.price AS total_price, cust.budget 
                                    FROM property prop
                                        INNER JOIN property_status stat ON prop.status_id = stat.status_id
                                        INNER JOIN sales_rep rep ON prop.emp_id = rep.emp_id
                                        INNER JOIN customer cust ON rep.emp_id = cust.emp_id
                                        
                                    WHERE (stat.status_name = 'LET AGREED' AND cust.intention = 'RENT' AND 
                                            cust.budget >= 1.05 * prop.price * 0.95)
                                    OR (stat.status_name = 'SOLD' AND cust.intention = 'BUY' AND 
                                        cust.budget >= 1.05 * prop.price * 0.95)
                                ;
                            """, con = conn_oltp)


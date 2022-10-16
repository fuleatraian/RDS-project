import random, names
from datetime import date

#This function groups together different postcodes with their specific city and returns a list of tuples
def area_generator(n):
    i = 0
    values = list()
    postcode = ["HP510ES", "HP260ES", "LN831NE", "LN208NE", "LN382NE", "TX135SW", "TX420SW",
                 "PD136NW", "PD813NW", "MD824NW", "MD981NW", "MK181SE"]
    while i < n:
        area_postcode = postcode[0]
        postcode.remove(area_postcode)
        if area_postcode in ["HP510ES", "HP260ES"]:
            city_id = 2
        elif area_postcode in ["LN831NE", "LN208NE", "LN382NE"]:
            city_id = 7
        elif area_postcode in ["TX135SW", "TX420SW", "PD136NW", "PD813NW"]:
            city_id = 8
        else:
            city_id = 5
        values.append((area_postcode, city_id))
        i += 1
    return values


def property_generation(n):
    i = 0
    values = list()
    areas = [1, 2, 3, 4, 5, 6, 7, 8]
    status = [1, 2, 3, 4]
    type = [1, 2, 3, 4, 5]
    while i < n:
        area_id = int(random.choice(areas))
        
        if area_id in [3, 4, 5]:
            emp_id = int(random.choice([12, 14, 18, 20]))
        elif area_id in [1, 2]:
            emp_id = int(random.choice([13, 17, 21]))
        elif area_id in [6, 7, 8]:
            emp_id = int(random.choice([15, 16, 19, 22]))
        
        type_id = int(random.choice(type))
        status_id = int(random.choice(status))

        if type_id in [1, 2, 3] and status_id in [1, 4]:
            no_bed = random.randint(1, 5)
            no_bath = random.randint(1, 3)
            price = no_bed * 30000 + no_bath * 15000
        elif type_id in [1, 2, 3] and status_id in [2, 3]:
            no_bed = random.randint(1, 5)
            no_bath = random.randint(1, 3)
            price = no_bed * 500 + no_bath * 150
        elif type_id in [4, 5]:
            no_bed = ''
            no_bath = ''
            price = random.randint(100000, 900000)
        
        values.append((area_id, type_id, no_bed, no_bath, price, status_id, emp_id))
        i += 1

    return values

def customer_generator(n):
    values = list()
    i = 0
    while i < n:
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        intention = random.choice(['BUY', 'SELL', 'RENT'])
        if intention == 'BUY':
            budget = random.randint(50000, 900000)
        elif intention == 'SELL':
            budget = ''
        else:
            budget = random.randint(500, 1500)
        emp_id = random.choice(list(range(12, 23)))
        values.append((first_name, last_name, budget, intention, emp_id))
        i += 1
    return values
    


def employee_generator(n):
    values = list()
    i = 0
    while i < n:
        if i < 11:
            dept_id = int(random.choice([1, 3, 5]))
        else:
            if i in [11, 13, 17, 19]:
                dept_id = 1
            elif i in [12, 16, 20]:
                dept_id = 3
            elif i in [14, 15, 18, 21]:
                dept_id = 5
        first_name = names.get_first_name(gender = 'male')
        last_name = names.get_last_name()
        gender = 'M'
        age = random.randint(25, 45)
        hire_date = date(year = random.randint(2000, 2020), month = random.randint(1, 12), day = random.randint(1, 28))
        values.append((dept_id, first_name, last_name, gender, age, hire_date))
        i += 1
        

    return values


def chief_generator(n):
    values = list()
    i = 0
    id = list(range(5, 12))
    areas_available = list(range(1, 9))
    while i < n:
        emp_id = random.choice(id)
        performance = round(random.uniform(0.0, 3.5), 1)
        target = round(random.uniform(1.5, 5), 1)
        area = random.choice(areas_available)
        rep_id = random.choice([1, 2])
        id.remove(emp_id)
        areas_available.remove(area)
        values.append((emp_id, performance, target, area, rep_id))
        i += 1
    return values


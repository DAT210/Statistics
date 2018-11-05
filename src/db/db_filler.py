import random
import mysql.connector
import subprocess

import faker.providers.date_time
import faker
import datetime

"""
    Script for creating dummy data to statistics database.
    Remark: Run db_init.sql to create database and tables before running this script!
"""

# Globale varibales for max/min values. All ID's start at 0.
MIN_SALARY, MAX_SALARY = 300000, 500000
MAX_ADDRESS_ID = 99
MAX_RESTAURANT_ID = 2
MAX_CUSTOMER_ID = 199
MAX_EMPLOYEE_ID = 29
MAX_PURCHASE_ID, MAX_PAYMENT_ID = 499, 499  # Needs to be equal
MAX_BOOKING_ID = 99
MAX_REVIEW_ID = 49
MAX_EVENT_ID = 49

INGREDIENTS = ["Flour", "Yeast", "Olive oil", "Tomato sauce", "Mozzarella", "Salami", "Chili", "Ruccola", "Prosciutto", "Onion", "Garlic", "Minced beef", "Bolognese sauce", \
    "Spaghetti", "Parmesan", "Bacon", "Egg", "Spaghetti", "Romaine salad", "Caesar dressing", "Chicken", "Brioche buns", "Cheddar", "Lettuce", "Burger dressing"]
MAX_INGREDIENT_ID = len(INGREDIENTS) - 1

COURSES = ["Pizza Margherita", "Pizza Diavola", "Pizza Prosciutto", "Pasta Bolognese", "Pasta Carbonara", "Caesar Salad", "Chicken Salad", "Fish and Chips", "Sushi", "Prawn soup", "Cheeseburger", "Baconburger"]
CATEGORIES =["Pizza", "Pizza", "Pizza", "Pasta", "Pasta", "Salad", "Salad", "Fish", "Fish", "Fish", "Burger", "Burger"]
MAX_COURSE_ID = len(COURSES) - 1

# Db connection
db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="dat210_statistics"
)

"""
    Creating fake data
"""
def create_fake_address(id, fake):
    return [{
        "address_id": id,
        "city": fake.city(),
        "postcode": fake.postcode(),
        "street_name": fake.street_name(),
        "street_number": random.randint(1, 999),
        "apartment_number": random.randint(1, 99)
    }]
def address(count, fake):
    address_list = []
    for i in range(count):
        address = create_fake_address(i, fake)
        address_list += address
    return address_list

def create_fake_restaurant(id, fake):
    return [{
        "restaurant_id": id,
        "restaurant_name": fake.first_name() + "'s restaurant",
        "phone": fake.phone_number(),
        "address_id": random.randint(0, MAX_ADDRESS_ID)
    }]
def restaurant(count, fake):
    restaurant_list = []
    for i in range(count):
        restaurant = create_fake_restaurant(i, fake)
        restaurant_list += restaurant
    return restaurant_list

def create_fake_customer(id, fake):
    return [{
        "customer_id": id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=100, tzinfo=None),
        "address_id": random.randint(0, MAX_ADDRESS_ID)
    }]
def customer(count, fake):
    customer_list = []
    for i in range(count):
        customer = create_fake_customer(i, fake)
        customer_list += customer
    return customer_list

def create_fake_employee(id, fake):
    return [{
        "employee_id": id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=67, tzinfo=None),
        "address_id": random.randint(0, MAX_ADDRESS_ID),
        "restaurant_id": random.randint(0, MAX_RESTAURANT_ID),
        "salary": random.randint(MIN_SALARY, MAX_SALARY),
        "start_date": fake.date_between(start_date=datetime.datetime(2017, 11, 1), end_date=datetime.datetime(2018, 11, 1))
    }]
def employee(count, fake):
    employee_list = []
    for i in range(count):
        employee = create_fake_employee(i, fake)
        employee_list += employee
    return employee_list

def courses(fake):
    course_list = []
    for i in range(len(COURSES)):
        course = [{
         "course_id": i,
         "course_name": COURSES[i],
         "price": random.randint(99, 199),
         "category": CATEGORIES[i],
         "information": fake.text(max_nb_chars=100, ext_word_list=None)
        }]
        course_list += course
    return course_list

def create_fake_booking(id, fake):
    return [{
        "booking_id": id,
        "restaurant_id": random.randint(0, MAX_RESTAURANT_ID),
        "table_id": random.randint(0, 19),
        "booking_date": fake.date_between(start_date=datetime.datetime(2017, 11, 1), end_date=datetime.datetime(2018, 11, 1)),
        "booking_length": random.randint(1, 6),
        "no_of_seats": random.randint(1, 19),
        "customer_id": random.randint(0, MAX_CUSTOMER_ID)
    }]
def bookings(count, fake):
    bookings =  []
    for i in range(count):
        booking = create_fake_booking(i, fake)
        bookings += booking
    return bookings

def create_fake_purchase(id, fake):
    price, tips, discount = random.randint(99, 999), random.randint(0, 99), random.uniform(0, 0.25)
    amount = (price + tips)*(1-discount)
    return[{
        "purchase_id": id,
        "purchase_time": fake.date_time_between(start_date=datetime.datetime(2017, 11, 1), end_date=datetime.datetime(2018, 11, 1), tzinfo=None), 
        "price": price,
        "order_ready": fake.date_time_between(start_date=datetime.datetime(2017, 11, 1), end_date=datetime.datetime(2018, 11, 1), tzinfo=None),
        "order_delivered": fake.date_time_between(start_date=datetime.datetime(2017, 11, 1), end_date=datetime.datetime(2018, 11, 1), tzinfo=None),
        "delivery_method": random.choice(["Inhouse", "Pickup", "Cycle", "Drone", "Car"]),
        "amount": amount,
        "tips": tips,
        "discount": discount,
        "address_id": random.randint(0, MAX_ADDRESS_ID),
        "customer_id": random.randint(0, MAX_CUSTOMER_ID),
        "payment_id": random.randint(0, MAX_PAYMENT_ID)
    }]

def purchases(count, fake):
    purchases =  []
    for i in range(count):
        purchase = create_fake_purchase(i, fake)
        purchases += purchase
    return purchases

def create_fake_review(id, fake):
    return [{
        "review_id": id,
        "course_id": random.randint(1, MAX_COURSE_ID),
        "review_text": fake.text(max_nb_chars=100, ext_word_list=None),
        "score": random.randint(1, 5)
    }]

def reviews(count, fake):
    reviews = []
    for i in range(count):
        review = create_fake_review(i, fake)
        reviews += review
    return reviews

def create_fake_s_event(id, fake):
    return [{
        "s_event_id": id,
        "event_date": fake.date_between(start_date=datetime.datetime(2017, 11, 1), end_date=datetime.datetime(2019, 11, 1)),
        "event_name": fake.first_name() + "'s event",
        "event_description": fake.text(max_nb_chars=100, ext_word_list=None)
    }]

def s_events(count, fake):
    events = []
    for i in range(count):
        event = create_fake_s_event(i, fake)
        events += event
    return events

def course_in_purchase(purchase_count, fake):
    course_in_purchases = []
    for purchase_id in range(purchase_count):
        
        # 3 courses in each purchase for convenience
        bound = int(MAX_COURSE_ID/3)
        course_in_purchase = {
            "purchase_id": purchase_id,
            "course_id": random.randint(0, bound),
            "quantity": random.randint(0, 4)
        }
        course_in_purchases.append(course_in_purchase)
        course_in_purchase = {
            "purchase_id": purchase_id,
            "course_id": random.randint(bound + 1, bound*2),
            "quantity": random.randint(0, 4)
        }
        course_in_purchases.append(course_in_purchase)
        course_in_purchase = {
            "purchase_id": purchase_id,
            "course_id": random.randint(bound*2 + 1, MAX_COURSE_ID),
            "quantity": random.randint(0, 4)
        }
        course_in_purchases.append(course_in_purchase)
    return course_in_purchases

def ingredients(fake):
    ingredient_list = []
    for i in range(len(INGREDIENTS)):
        ingredient = {
         "ingredient_id": i,
         "ingredient_name": INGREDIENTS[i],
         "information": fake.text(max_nb_chars=100, ext_word_list=None)
        }
        ingredient_list.append(ingredient)
    return ingredient_list

def allergenes(fake):
    allergenes = ["Gluten", "Egg", "Milk"]
    allergene_list = []
    for i in range(len(allergenes)):
        allergene = {
         "allergene_id": i,
         "allergene_name": allergenes[i]
        }
        allergene_list.append(allergene)
    return allergene_list

def stock(restaurant_count, ingredient_count):
    stocks = []
    for r_id in range(restaurant_count):
        for i_id in range(ingredient_count):
            s = {
                "restaurant_id": r_id, 
                "ingredient_id": i_id,
                "quantity": random.randint(0, 49)
            }
            stocks.append(s)
    return stocks

def ingredients_in_course(course_list, ingredient_list):
    iic_list = []
    for course in course_list:
        # For convenience every course will have 4 ingredients, with all sorts of weird combos
        bound = int(MAX_INGREDIENT_ID/4)
        iic = {
            "course_id": course["course_id"],
            "ingredient_id": random.randint(0, bound)
        }
        iic_list.append(iic)
        iic = {
            "course_id": course["course_id"],
            "ingredient_id": random.randint(bound + 1, bound*2)
        }
        iic_list.append(iic)
        iic = {
            "course_id": course["course_id"],
            "ingredient_id": random.randint(bound*2 +1, bound*3)
        }
        iic_list.append(iic)
        iic = {
            "course_id": course["course_id"],
            "ingredient_id": random.randint(bound*3 + 1, MAX_INGREDIENT_ID)
        }
        iic_list.append(iic)
    return iic_list

def allergene_in_ingredient():
    aii_list = [
        {
            "ingredient_id": 0, # Flour
            "allergene_id": 0 # Gluten
        }, 
        {
            "ingredient_id": 16, # Egg
            "allergene_id": 1 # Egg
        }, 
        {
            "ingredient_id": 19, # Caesar dressing
            "allergene_id": 1 # Egg
        },
        {
            "ingredient_id": 19, # Caesar dressing
            "allergene_id": 2 # Milk
        },  
        {
            "ingredient_id": 21, # Brioche buns
            "allergene_id": 0 # Gluten
        }, 
        {
            "ingredient_id": 24, # Burger dressing
            "allergene_id": 1 # Egg 
        },
        {
            "ingredient_id": 24, # Burger dressing
            "allergene_id": 2 # Milk 
        }
    ]
    return aii_list

"""
    Inserting to database
"""
def insert_addresses(address_list):
    success = True
    for address in address_list:
        cur = db_conn.cursor()
        sql = ("INSERT INTO address(address_id, city, postcode, street_name, street_number, apartment_number) VALUES(%s, %s, %s, %s, %s, %s)")
        try:
            cur.execute(sql, (address["address_id"], address["city"], address["postcode"], address["street_name"], address["street_number"], address["apartment_number"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Addresses: Successfully inserted to db.")

def insert_restaurants(restaurant_list):
    success = True
    for restaurant in restaurant_list:
        cur = db_conn.cursor()
        sql = ("INSERT INTO restaurant(restaurant_id, restaurant_name, phone, address_id) VALUES(%s, %s, %s, %s)")
        try:
            cur.execute(sql, (restaurant["restaurant_id"], restaurant["restaurant_name"], restaurant["phone"], restaurant["address_id"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Restaurants: Successfully inserted to db.")

def insert_customers(customer_list):
    success = True
    for customer in customer_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO customer(customer_id, first_name, last_name, email, phone, birthdate, address_id) VALUES(%s, %s, %s, %s, %s, %s, %s)")
        try:
            cur.execute(sql, (customer["customer_id"], customer["first_name"], customer["last_name"], customer["email"], customer["phone"], customer["birthdate"], customer["address_id"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Customers: Successfully inserted into db.")

def insert_employees(employee_list):
    success = True
    for employee in employee_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO employee(employee_id, first_name, last_name, email, phone, birthdate, address_id, restaurant_id, salary, start_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        try:
            cur.execute(sql, (employee["employee_id"], employee["first_name"], employee["last_name"], employee["email"], employee["phone"], employee["birthdate"], employee["address_id"], employee["restaurant_id"], employee["salary"], employee["start_date"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Customers: Successfully inserted into db.")

def insert_courses(course_list):
    success = True
    for course in course_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO course(course_id, course_name, price, category, information) VALUES(%s, %s, %s, %s, %s)")
        try:
            cur.execute(sql, (course["course_id"], course["course_name"],course["price"], course["category"], course["information"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Courses: Successfully inserted to db.")

def insert_bookings(booking_list):
    success = True
    for booking in booking_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO booking(booking_id, restaurant_id, table_id, booking_date, booking_length, no_of_seats, customer_id) VALUES(%s, %s, %s, %s, %s, %s, %s)")
        try:
            cur.execute(sql, (booking["booking_id"], booking["restaurant_id"], booking["table_id"], booking["booking_date"], booking["booking_length"], booking["no_of_seats"], booking["customer_id"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Bookings: Successfully inserted to db.")

def insert_purchases(purchase_list):
    success = True
    for purchase in purchase_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO purchase(purchase_id, purchase_time, price, order_ready, order_delivered, delivery_method, \
        amount, tips, discount, address_id, customer_id, payment_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        try:
            cur.execute(sql, (purchase["purchase_id"], purchase["purchase_time"], purchase["price"], purchase["order_ready"],\
            purchase["order_delivered"], purchase["delivery_method"], purchase["amount"], purchase["tips"], purchase["discount"], \
            purchase["address_id"], purchase["customer_id"], purchase["payment_id"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Purchases: Successfully inserted to db.")

def insert_reviews(review_list):
    success = True
    for review in review_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO review(review_id, course_id, review_text, score) VALUES(%s, %s, %s,%s)")
        try:
            cur.execute(sql, (review["review_id"], review["course_id"], review["review_text"], review["score"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Reviews: Successfully inserted to db.")

def insert_s_events(event_list):
    success = True
    for event in event_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO s_event(s_event_id, event_date, event_name, event_description) VALUES(%s, %s, %s, %s)")
        try:
            cur.execute(sql, (event["s_event_id"], event["event_date"], event["event_name"], event["event_description"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Events: Successfully inserted to db.")

def insert_course_in_purchase(cip_list):
    success = True
    for cip in cip_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO course_in_purchase(purchase_id, course_id, quantity) VALUES(%s, %s, %s)")
        try:
            cur.execute(sql, (cip["purchase_id"], cip["course_id"], cip["quantity"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            print(cip)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Course in purchase: Successfully inserted to db.")



def insert_ingredients(ingredient_list):
    success = True
    for ingredient in ingredient_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO ingredient(ingredient_id, ingredient_name) VALUES(%s, %s)")
        try:
            cur.execute(sql, (ingredient["ingredient_id"], ingredient["ingredient_name"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Ingredients: Successfully inserted to db.")

def insert_allergenes(allergene_list):
    success = True
    for allergene in allergene_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO allergene(allergene_id, allergene_name) VALUES(%s, %s)")
        try:
            cur.execute(sql, (allergene["allergene_id"], allergene["allergene_name"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Allergenes: Successfully inserted to db.")

def insert_stock(stock_list):
    success = True
    for stock in stock_list:
        cur = db_conn.cursor()      
        sql = ("INSERT INTO stock(restaurant_id, ingredient_id, quantity) VALUES(%s, %s, %s)")
        try:
            cur.execute(sql, (stock["restaurant_id"], stock["ingredient_id"], stock["quantity"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Stocks: Successfully inserted to db.")

def insert_allergene_in_ingredient(ai_list):
    success = True
    for entry in ai_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO allergene_in_ingredient(ingredient_id, allergene_id) VALUES(%s, %s)")
        try:
            cur.execute(sql, (entry["ingredient_id"], entry["allergene_id"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Allergene in ingredients: Successfully inserted to db.")

def insert_ingredient_in_course(ic_list):
    success = True
    for entry in ic_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO ingredient_in_course(course_id, ingredient_id) VALUES(%s, %s)")
        try:
            cur.execute(sql, (entry["course_id"], entry["ingredient_id"]))
            db_conn.commit()
        except mysql.connector.Error as err:
            print("Oops, something went wrong with db insert:", err)
            success = False
        finally:
            cur.close()
    if success == True:
        print("Ingredients in courses: Successfully inserted to db.")

def main():
    fake = faker.Faker("no_NO")   # no_NO: Norwegian language and units
    
    # Set seeds: Script can be run multiple times and produce same data 
    fake.seed(4321)
    random.seed(1234)

    # Create lists of fake values
    address_list = address(MAX_ADDRESS_ID + 1, fake)
    customer_list = customer(MAX_CUSTOMER_ID + 1, fake)
    restaurant_list = restaurant(MAX_RESTAURANT_ID + 1, fake)
    employee_list = employee(MAX_EMPLOYEE_ID + 1, fake)
    course_list = courses(fake)
    booking_list = bookings(MAX_BOOKING_ID + 1, fake)
    purchase_list = purchases(MAX_PURCHASE_ID + 1, fake)
    review_list = reviews(MAX_REVIEW_ID + 1, fake)
    s_event_list = s_events(MAX_EVENT_ID + 1, fake)
    cip_list = course_in_purchase(MAX_PURCHASE_ID + 1, fake)
    ingredient_list = ingredients(fake)
    allergene_list = allergenes(fake)
    stock_list = stock(len(restaurant_list), len(ingredient_list))

    # Insert into db
    insert_addresses(address_list)
    insert_customers(customer_list)
    insert_restaurants(restaurant_list)
    insert_employees(employee_list)
    insert_courses(course_list)
    insert_bookings(booking_list)
    insert_purchases(purchase_list)
    insert_reviews(review_list)
    insert_s_events(s_event_list)
    insert_course_in_purchase(cip_list)
    insert_ingredients(ingredient_list) 
    insert_allergenes(allergene_list)
    insert_stock(stock_list) 
    insert_allergene_in_ingredient(allergene_in_ingredient())
    insert_ingredient_in_course(ingredients_in_course(course_list, ingredient_list))
    
    # Dumps the statistics database to a sql-file. Outsources the subprocess to shellscript. File is dumped to the project root-folder
    subprocess.Popen("mysqldump --host=localhost --port=3306 --user=root --password=root dat210_statistics > dump.sql", shell=True)

if __name__ == '__main__':
    main()

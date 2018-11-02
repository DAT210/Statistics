import random
import mysql.connector
import subprocess

import faker.providers.date_time
import faker

# Remark: Script currently requires a precreated DB with no values to exist. Run db_init.sql beforehand!

# Globale varibales for max/min values. All ID's start at 0.
MIN_SALARY, MAX_SALARY = 300000, 500000
MAX_ADDRESS_ID = 99
MAX_RESTAURANT_ID = 2
MAX_CUSTOMER_ID = 199
MAX_EMPLOYEE_ID = 29
MAX_PURCHASE_ID, MAX_PAYMENT_ID = 499, 499   # Needs to be equal
MAX_BOOKING_ID = 99
MAX_REVIEW_ID = 49
MAX_EVENT_ID = 49

# Db connection created
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
        "birthdate": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100),
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
        "birthdate": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=67),
        "address_id": random.randint(0, MAX_ADDRESS_ID),
        "restaurant_id": random.randint(0, MAX_RESTAURANT_ID),
        "salary": random.randint(MIN_SALARY, MAX_SALARY),
        "start_date": fake.past_date(start_date="-1y", tzinfo=None)
        # Use instead: fake.past_datetime(start_date="2017-11-01", tzinfo=None) ??
    }]
def employee(count, fake):
    employee_list = []
    for i in range(count):
        employee = create_fake_employee(i, fake)
        employee_list += employee
    return employee_list

def courses(fake):
    courses = ["Pizza Margherita", "Pizza Diavola", "Pizza Prosciutto", "Pasta Bolognese", "Pasta Carbonara", "Caesar Salad", "Chicken Salad", "Fish and Chips", "Sushi", "Prawn soup", "Cheeseburger", "Baconburger"]
    categories =["Pizza", "Pizza", "Pizza", "Pasta", "Pasta", "Salad", "Salad", "Fish", "Fish", "Fish", "Burger", "Burger"]
    course_list = []
    for i in range(len(courses)):
        course = [{
         "course_id": i,
         "course_name": courses[i],
         "price": random.randint(99, 199),
         "category": categories[i],
         "information": fake.text(max_nb_chars=100, ext_word_list=None)
        }]
        course_list += course
    return course_list

def create_fake_booking(id, fake):
    return [{
        "booking_id": id,
        "restaurant_id": random.randint(0, MAX_RESTAURANT_ID),
        "table_id": random.randint(0, 19),
        "booking_date": fake.past_date(start_date="-1y", tzinfo=None),
        "booking_length": random.randint(1, 6),
        "no_of_seats": random.randint(1, 19),
        "customer_id": random.randint(0, MAX_CUSTOMER_ID)
        # Use instead: fake.past_date(start_date="2017-11-01") ??
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
        "purchase_time": fake.past_datetime(start_date="-1y", tzinfo=None), 
        "price": price,
        "order_ready": fake.past_datetime(start_date="-1y", tzinfo=None),
        "order_delivered": fake.past_datetime(start_date="-1y", tzinfo=None),
        "delivery_method": random.choice(["Inhouse", "Pickup", "Cycle", "Drone", "Car"]),
        "amount": amount,
        "tips": tips,
        "discount": discount,
        "address_id": random.randint(0, MAX_ADDRESS_ID),
        "customer_id": random.randint(0, MAX_CUSTOMER_ID),
        "payment_id": random.randint(0, MAX_PAYMENT_ID)
        # Use instead: fake.past_datetime(start_date="2017-11-01", tzinfo=None) ??
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
        "course_id": random.randint(1, 11), # 11 = MAX_COURSE_ID atm. May need update
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
        "event_date": fake.date_between(start_date="-1y", end_date="+1y"),
        "event_name": fake.first_name() + "'s event",
        "event_description": fake.text(max_nb_chars=100, ext_word_list=None)
    }]

def s_events(count, fake):
    events = []
    for i in range(count):
        event = create_fake_s_event(i, fake)
        events += event
    return events


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
        print("Purchase: Successfully inserted to db.")

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
        print("Review: Successfully inserted to db.")

def insert_s_event(event_list):
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
        print("Event: Successfully inserted to db.")

def main():
    fake = faker.Faker("no_NO")   # no_NO: Norwegian language and units
    
    # Set seeds: Script can be run multiple times and produce same data 
    fake.seed(4321)
    random.seed(1234)

    # Create list of fake values
    address_list = address(MAX_ADDRESS_ID + 1, fake)
    customer_list = customer(MAX_CUSTOMER_ID + 1, fake)
    restaurant_list = restaurant(MAX_RESTAURANT_ID + 1, fake)
    employee_list = employee(MAX_EMPLOYEE_ID + 1, fake)
    course_list = courses(fake)
    booking_list = bookings(MAX_BOOKING_ID + 1, fake)
    purchase_list = purchases(MAX_PURCHASE_ID + 1, fake)
    review_list = reviews(MAX_REVIEW_ID + 1, fake)
    s_event_list = s_events(MAX_EVENT_ID + 1, fake)

    # Insert into db
    insert_addresses(address_list)
    insert_customers(customer_list)
    insert_restaurants(restaurant_list)
    insert_employees(employee_list)
    insert_courses(course_list)
    insert_bookings(booking_list)
    insert_purchases(purchase_list)
    insert_reviews(review_list)
    insert_s_event(s_event_list)
    
    # Dumps the statistics database to a sql-file. Outsources the subprocess to shellscript. File is dumped to the project root-folder
    # subprocess.Popen("mysqldump --host=localhost --port=3306 --user=root --password=root dat210_statistics > dump.sql", shell=True)
   

if __name__ == '__main__':
    main()

import random
import mysql.connector
import subprocess

import faker.providers.date_time
from faker import Factory

#Script currently requires a precreated DB to exist.
DB_NAME = "statistics"
db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database=DB_NAME
)

TABLES = {}
TABLES['customer'] = (
    "CREATE TABLE IF NOT EXISTS `customer`("
        "`customer_id` int(9) NOT NULL AUTO_INCREMENT,"
        "`f_name` varchar(20) DEFAULT NULL,"
        "`s_name` varchar(30) DEFAULT NULL,"
        "`phone` int(11) DEFAULT NULL,"
        "`birthdate` date DEFAULT NULL,"
        "`email` varchar(50) DEFAULT NULL,"
        "`c_address` varchar(100) DEFAULT NULL,"
        "PRIMARY KEY (`customer_id`)"
        ") ENGINE=InnoDB"
)
TABLES['dish'] = (
    "CREATE TABLE IF NOT EXISTS `dish` ("
        "`dish_id` int(9) NOT NULL AUTO_INCREMENT,"
        "`dish_name` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,"
        "`price` int(9) DEFAULT NULL,"
        "PRIMARY KEY (`dish_id`)"
        ") ENGINE=InnoDB"
)
TABLES['orders'] = (
    "CREATE TABLE IF NOT EXISTS `orders`("
        "`order_id` INT(9) AUTO_INCREMENT,"
        "`time_stamp` TIME,"
        "`date` DATE,"
        "`order_type` VARCHAR(20),"
        "`customer_id` INT(9),"
        "`dish_id` INT(9),"
        "`delivery` VARCHAR(32) DEFAULT NULL,"
        "`price` INT(9) DEFAULT NULL,"
        "PRIMARY KEY (`order_id`),"
        "CONSTRAINT `dish_id_ibfk1` FOREIGN KEY (`dish_id`) REFERENCES `dish` (`dish_id`),"
        "CONSTRAINT `customer_id_ibfk2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)"
        ") ENGINE=InnoDB"
)

def create_fake_customer(id, fake):
    return [{
        "id": id + 1,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone": fake.numerify("########"),
        "date": fake.date(),
        "email": fake.email(),
        "address": fake.address()
    }]

def customer(count, fake):
    customer_list = []
    for i in range(count):
        customer = create_fake_customer(i, fake)
        customer_list += customer
    return customer_list


def create_dishes(fake):
    dishes = ["Pepperoni Pizza", "Pasta Bolognese", "Ribeye", "French Onion Soup", "Cesar Salad", "Fish and Chips", "Sushi", "Bibimbap", "Cheeseburger", "Yemista", "Roasted Lamb"]
    dishes_list = []
    for i in range(len(dishes)):
        dish = [{
         "id": i + 1,
         "dish_name": dishes[i],
         "price": fake.numerify("###")
        }]
        dishes_list += dish
    return dishes_list


def create_fake_order(id, fake, customer_count, dish_count):
    return[{
        "id": id + 1,
        "time_stamp": fake.time(),
        "date": fake.date_between(start_date='-1y', end_date='today'),
        "order_type": random.choice(["inhouse", "take-away"]),
        "customer_id": random.randint(1, customer_count),
        "dish_id": random.randint(1, dish_count),
        "delivery": random.choice(["Pickup", "Cycle", "Drone", "Car", "Customer"]),
        "price": random.randint(50, 999)
    }]

def orders(count, fake, customer_count, dish_count):
    orders =  []
    for i in range(count):
        order = create_fake_order(i, fake, customer_count, dish_count)
        orders += order
    return orders

def create_tables():
    cur = db_conn.cursor()
    for table_name in TABLES:
        table_description = TABLES[table_name]
        print("Creating table {}\n ".format(table_name), end='')
        cur.execute(table_description)
    cur.close()

def insert_customers(customer_list):
    for customer in customer_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO customer(f_name, s_name, phone, birthdate, email, c_address) VALUES(%s, %s, %s, %s, %s, %s)")
        cur.execute(sql, (customer['first_name'], customer['last_name'], customer['phone'], customer['date'], customer['email'], customer['address']))
        db_conn.commit()
        cur.close()
    print("Customers inserted into database")

def insert_dishes(dishes_list):
    for dish in dishes_list:
        cur = db_conn.cursor()        
        sql = ("INSERT INTO dish(dish_name, price) VALUES(%s, %s)")
        cur.execute(sql, (dish['dish_name'], dish['price']))
        db_conn.commit()
        cur.close()
    print("Dishes inserted into database")

def insert_orders(orders_list):
    for order in orders_list:
        cur = db_conn.cursor()
        sql = ("INSERT INTO orders(time_stamp, date, order_type, customer_id, dish_id, delivery, price) VALUES(%s, %s, %s, %s, %s, %s, %s)")
        cur.execute(sql, (order['time_stamp'], order['date'], order['order_type'], order['customer_id'], order['dish_id'], order['delivery'], order['price']))
        db_conn.commit()
        cur.close()
    print("Orders inserted into database")

def main():
    fake = Factory.create()
    customer_list = customer(50, fake)
    dishes_list = create_dishes(fake)
    orders_list = orders(250, fake, len(customer_list), len(dishes_list))

    create_tables()
    insert_customers(customer_list)
    insert_dishes(dishes_list)
    insert_orders(orders_list)
    
    #Dumps the statistics database to a sql-file. Outsources the subprocess to shellscript. File is dumped to the project root-folder
    subprocess.Popen('mysqldump --host=localhost --port=3306 --user=root --password=root statistics > dump.sql', shell=True)
   

if __name__ == '__main__':
    main()

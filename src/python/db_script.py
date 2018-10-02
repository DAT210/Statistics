import mysql.connector
import pandas
import random
from faker import Factory, Faker


faker = Factory.create()
fake = Faker()
fake.seed(1234)
status = 'created,delivered,returned'.split(',')

def date_between(d1, d2):
    f = '%b%d-%Y'
    return faker.date_time_between_dates(datetime.strptime(d1, f), datetime.strptime(d2, f))

def fakecustomer():
    name = fake.name().split(" ")
    return {'f_name': name[0],  # random cities
            's_name': name[1],  # different products
            'phone': faker.numerify('########'),  # different categories
            'birthdate': date_between('jan10-1950', 'dec30-2015'), #random date between the specified dates
            'email': name[1] + name[0] + "@test.co.cc",
            'c_address': faker.city(),
            }
    
db = mysql.connector.connect(host="localhost",      # your host, usually localhost
                     user="root",           # your username
                     passwd="root",         # your password
                     db="statistics")       # name of the data base

cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS customer_test(
                customer_id INT(9) AUTO_INCREMENT,
                f_name VARCHAR(20),
                s_name VARCHAR(30),
                phone INTEGER,
                birthdate VARCHAR(20),
                email VARCHAR(50),
                c_address VARCHAR(100),
                PRIMARY KEY(customer_id)
                )ENGINE=InnoDB;"""
            )

cur.execute("""INSERT INTO customer(f_name, s_name, phone, birthdate, email, c_address)
VALUES('Ola', 'Nordmann', 12345678, '1945-04-09', 'N/A', 'Slottsplassen 1'),\
      ('Trude', 'Dali', 324324278, '1914-05-07', 'dali@gmail.com', 'Bryggen 51'),\
      ('Kari', 'Sjeldbrei', 322342678, '2014-06-06', 'sugarbaby@hacks.co', 'Langata 52'),\
      ('Sara', 'Wathne', 32455688, '2013-08-23', 'swathne92@hotmail.com', 'Fargegaten 52');""")

# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
#for row in cur.fetchall():
#    print row[0]

db.close()
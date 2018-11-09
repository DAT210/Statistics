import mysql.connector
import json
import collections
import app

# Includes all customer related functions

def get_customer(customer_id):
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM customer WHERE customer_id = %s;"
        cur.execute(sql, (customer_id,))
        customer = cur.fetchone()

        if customer == None:
            raise NameError("This customer_id doesn\'t exist in the database")
        else:
            customer_info = {
                "customer_id": customer_id,
                "first_name": customer[1],
                "last_name": customer[2],
                "email": customer[3],
                "phone": customer[4],
                "birthdate": customer[5],
                "address_id": customer[6]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(customer_info)

def get_all_customers():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM customer"
        cur.execute(sql)

        customers = []
        for customer in cur.fetchall():
            new = {
                "customer_id": customer[0],
                "first_name": customer[1],
                "last_name": customer[2],
                "email": customer[3],
                "phone": customer[4],
                "birthdate": customer[5],
                "address_id": customer[6]
            } 
            customers.append(new)
        if len(customers) <= 0:
            print("No customers in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return customers # Do not json.dumps() this. Need a python dict in Jinja
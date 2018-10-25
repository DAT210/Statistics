import mysql.connector
import json
import collections
import app

# this will execute a function to input data to DB based
# on the "input_type" field of the POST request
def input(json_content):
    content = json.load(json_content)
    {"completed_order" : completed_order,
    "other_input" : other_input,
    "new_customer": insert_new_customer,
    "new_booking": insert_new_booking,
    "new_employee": insert_new_employee
    # add new funtions for all types of input
    }[content["input_type"]](content)


def completed_order(content):
    return


def other_input(content):
    return


def insert_new_customer(content):
    db = app.get_db()
    cur = db.cursor()
    try:
        sql_address = "INSERT INTO address(city, postcode, street_name, street_number, apartment_number) VALUES(%s, %s, %s, %s, %s, %s)"
        cur.execute(sql_address, (content["city"], content["postcode"], content["street_name"], content["street_number"], content["apartment_number"]))
    
        sql = "SELECT address_id, apartment_number FROM address WHERE city=%s AND postcode=%s AND street_name=%s AND street_number=%s"
        cur.execute(sql, (content["city"], content["postcode"], content["street_name"], content["street_number"]), )
        address_list = cur.fetchall()
        if len(address_list) > 1:
            for address in address_list:
                if address[1] == content["apartment_number"]:
                    address_id = address[0]
        
        sql_customer = "INSERT INTO customer(first_name, last_name, email, phone, birthdate, address_id) VALUES(%s, %s, %s, %s, %s, %s, %s);"
        cur.execute(sql_customer, (content["first_name"], content["last_name"], content["email"], content["phone"], content["birthdate"], address_id))

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()

    return 0


def insert_new_booking(content):
    db = app.get_db()
    cur = db.cursor()
    try:
        sql_restaurant = "SELECT restaurant_id FROM restaurant WHERE restaurant_name=%s"
        cur.execute(sql_restaurant, content["restaurant_name"])
        restaurant_id = cur.fetchone()

        sql_customer = "SELECT customer_id FROM customer WHERE first_name=%s AND last_name=%s"
        cur.execute(sql_customer, (content["first_name"], content["last_name"]))
        customer_id = cur.fetchone()

        sql_booking = "INSERT INTO booking(restaurant_id, table_id, booking_date, booking_length, no_of_seats, customer_id) VALUES(%s, %s, %s, %s, %s, %s);"
        cur.execute(sql_booking, (restaurant_id, content["table_id"], content["booking_date"], content["booking_length"], content["no_of_seats"], customer_id))

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()

    return 0


def insert_new_employee(content):
    db = app.get_db()
    cur = db.cursor()
    try:
        sql_restaurant = "SELECT restaurant_id FROM restaurant WHERE restaurant_name=%s"
        cur.execute(sql_restaurant, content["restaurant_name"])
        restaurant_id = cur.fetchone()

        sql_address = "SELECT address_id, apartment_number FROM address WHERE city=%s AND postcode=%s AND street_name=%s AND street_number=%s"
        cur.execute(sql_address, (content["city"], content["postcode"], content["street_name"], content["street_number"]), )
        address_list = cur.fetchall()
        if len(address_list) > 1:
            for address in address_list:
                if address[1] == content["apartment_number"]:
                    address_id = address[0]
        
        sql_employee = "INSERT INTO employee(first_name, last_name, email, phone, birthdate, address_id, restaurant_id, salary, start_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cur.execute(sql_employee, (content["first_name"], content["last_name"], content["email"], content["phone"], content["birthdate"], address_id, restaurant_id, content["salary"], content["start_date"]))

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()

    return 0

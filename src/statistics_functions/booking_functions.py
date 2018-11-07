import mysql.connector
import json
import collections
import app

# Includes all booking related functions

def get_booking(booking_id):
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM booking WHERE booking_id = %s;"
        cur.execute(sql, (booking_id))
        booking = cur.fetchone()

        if booking == None:
            raise NameError("This booking_id doesn\'t exist in the database")
        else:
            booking_info = {
                "booking_id": booking_id,
                "restaurant_id": booking[1],
                "table_id": booking[2],
                "booking_date": booking[3],
                "booking_length": booking[4],
                "no_of_seats": booking[5],
                "customer_id": booking[6]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(booking_info)


def booking_per_restaurant():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT DISTINCT restaurant_id FROM booking ORDER BY restaurant_id;"
        cur.execute(sql)
        booking = []
        for restaurant_id in cur.fetchall():
            sql_booking_per_restaurant = "SELECT COUNT(*) FROM booking WHERE restaurant_id = %s;"
            cur.execute(sql_booking_per_restaurant, (restaurant_id))
            total_bookings = cur.fetchone()
            new = {
                "restaurant_id": restaurant_id[0],
                "total_bookings": total_bookings[0]
            }
            booking.append(new)
        print(booking)
        if len(booking) <= 0:
            print("No bookings in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(booking)


def ingredients_per_restaurant_stock():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT DISTINCT restaurant_id FROM booking ORDER BY restaurant_id;"
        cur.execute(sql)
        stock = []
        for restaurant_id in cur.fetchall():
            sql_ingredient_list_per_restaurant = "SELECT ingredient_id, quantity FROM stock WHERE restaurant_id = %s;"
            cur.execute(sql_ingredient_list_per_restaurant, (restaurant_id))
            total_stock = cur.fetchone()
            new = {}
            for ingredient in total_stock:
                sql_ingredient_name = "SELECT ingredient_name FROM ingredient WHERE ingredient_id = %s;"
                ingredient_name = cur.execute(sql_ingredient_name, (ingredient[0]))

                new [ingredient[0]] = {
                    "ingredient_name": ingredient_name,
                    "quantity": ingredient[1]
                }
            stock.append(new)
        print(stock)
        if len(stock) <= 0:
            print("No stocks in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return 0

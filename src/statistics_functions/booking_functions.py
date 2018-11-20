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
        cur.execute(sql, (booking_id,))
        booking = cur.fetchone()

        if booking == None:
            raise NameError("This booking_id doesn\'t exist in the database")
        else:
            booking_info = {
                "booking_id": booking_id,
                "restaurant_id": booking[1],
                "table_id": booking[2],
                "booking_date": booking[3].isoformat(),
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
        all_stocks = {}
        for restaurant_id in cur.fetchall():
            sql_ingredient_list_per_restaurant = "SELECT ingredient_id, quantity FROM stock WHERE restaurant_id = %s ORDER BY ingredient_id;"
            cur.execute(sql_ingredient_list_per_restaurant, (restaurant_id))
            stock = []
            total_stock = cur.fetchall()
            for ingredient in total_stock:
                id = ingredient[0]
                cur.execute("SELECT ingredient_name FROM ingredient WHERE ingredient_id = %s;" % (id) )
                new = {
                    "ingredient_id": id,
                    "ingredient_name": cur.fetchone()[0],
                    "quantity": ingredient[1]
                }
                stock.append(new)
            all_stocks[restaurant_id[0]] = stock
            if len(stock) <= 0:
                print("No stocks in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(all_stocks)

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
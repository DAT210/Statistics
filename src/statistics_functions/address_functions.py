import mysql.connector
import json
import collections
import app

# Includes all address related functions

def get_address(address_id):
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM address WHERE address_id = %s;"
        cur.execute(sql, (address_id,))
        address = cur.fetchone()

        if address == None:
            raise NameError("This address_id doesn\'t exist in the database")
        else:
            address_info = {
                "address_id": address_id,
                "city": address[1],
                "postcode": address[2],
                "street_name": address[3],
                "street_number": address[4],
                "apartment_number": address[5]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(address_info)
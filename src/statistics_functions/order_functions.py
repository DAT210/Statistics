import mysql.connector
import json
import collections
import app

# Includes all order related functions

def get_all_orders():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM purchase;"
        cur.execute(sql)

        orders = []
        for order in cur.fetchall():
            new = {
                "order_id": order[0],
                "time_of_purchase": order[1],
                "price": order[2],
                "order_ready": order[3],
                "order_delivered": order[4],
                "delivery_method": order[5],
                "address_id": order[6],
                "total_amount_payed": order[7],
                "tips": order[8],
                "discount": order[9],
                "customer_id": order[10],
                "payment_id": order[11]
            }
            orders.append(new)
        if len(orders) <= 0:
            print("No orders in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(orders)

def orders_per_month(): # Ikke fullstendig omskrevet enda, må testes
    orders = get_all_orders()
    res = {}
    for order in orders:
        curr_month = order["time_of_purchase"].month
        if curr_month in res:
            res[curr_month] += 1
        else:
            res[curr_month] = 1

    res = collections.OrderedDict(sorted(res.items()))  # Sort result based on month number

    months = {1: "January", 2: "February", 3: "Mars", 4: "April", 5: "May", 6: "June", 
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    res_names = {}  # New dict with month names instead of numbers
    for num, count in res.items():
        month = months[num]   
        res_names[month] = count
    return json.dumps(res_names)

def courses_sold():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql_courses_sold = "SELECT course_id, count(*) as total_sold FROM course_in_purchase GROUP BY course_id;"
        cur.execute(sql_courses_sold)
        courses = cur.fetchall()

        sql_name_of_course = "SELECT course_name FROM course WHERE course_id =%s;"
        total_sold = []
        for course_id, count in courses:
            cur.execute(sql_name_of_course, course_id)
            name = cur.fetchone()
            course = {
                "course_id": course_id,
                "course_name": name,
                "amount_sold": count
            }
            total_sold.append(course)
        
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(total_sold)

def get_order(order_id):

    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM purchase WHERE purchase_id=%s;"
        cur.execute(sql, (order_id))

        order = cur.fetchone()
        if order == None:
            raise NameError("This order_id doesn\'t exist in our database")
        else:
            order_info = {
                "order_id": order[0],
                "time_of_purchase": order[1],
                "price": order[2],
                "order_ready": order[3],
                "order_delivered": order[4],
                "delivery_method": order[5],
                "address_id": order[6],
                "total_amount_payed": order[7],
                "tips": order[8],
                "discount": order[9],
                "customer_id": order[10],
                "payment_id": order[11]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(order_info)

def orders_per_day():
    db = app.get_db()
    cur = db.cursor()
    try:

        sql = "SELECT purchase_time FROM purchase;"
        cur.execute(sql)
        days = []
        for purchase_time in cur.fetchall():
            sql_how_many_per_day = "SELECT COUNT(*) as total_orders FROM purchase WHERE purchase_time >= DATE_SUB(%s, INTERVAL 0 DAY);"
            cur.execute(sql_how_many_per_day, (purchase_time.date))
            total_orders = cur.fetchone()
            new = {
                "time_of_purchase": purchase_time,
                "total_orders": total_orders,
            }
            days.append(new)
        if len(days) <= 0:
            print("No orders in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(days)

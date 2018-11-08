import mysql.connector
import json
import collections
import app

# Includes all purchase related functions

def get_all_purchases():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM purchase;"
        cur.execute(sql)

        purchases = []
        for purchase in cur.fetchall():
            new = {
                "purchase_id": purchase[0],
                "time_of_purchase": purchase[1],
                "price": purchase[2],
                "order_ready": purchase[3],
                "order_delivered": purchase[4],
                "delivery_method": purchase[5],
                "address_id": purchase[6],
                "total_amount_payed": round(purchase[7], 2),
                "tips": purchase[8],
                "discount": str(round(purchase[9]*100, 0)) + "%",
                "customer_id": purchase[10],
                "payment_id": purchase[11]
            }
            purchases.append(new)
        if len(purchases) <= 0:
            print("No purchases in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return purchases # Do not json.dumps() this. Need a python dict in Jinja

def purchases_per_month(): # Ikke fullstendig omskrevet enda, må testes
    purchases = get_all_purchases()
    res = {}
    for purchase in purchases:
        curr_month = purchase["time_of_purchase"].month
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

        sql_name_of_course = "SELECT course_name FROM course WHERE course_id=%s;"
        total_sold = []
        for course_id, count in courses:
            cur.execute(sql_name_of_course, (course_id,))
            name = cur.fetchone()
            course = {
                "course_id": course_id,
                "course_name": name[0],
                "amount_sold": count
            }
            total_sold.append(course)
        print(total_sold)
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(total_sold)

def get_purchase(purchase_id):

    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM purchase WHERE purchase_id=%s;"
        cur.execute(sql, (purchase_id,))

        purchase = cur.fetchone()
        if purchase == None:
            raise NameError("This purchase_id doesn\'t exist in our database")
        else:
            purchase_info = {
                "purchase_id": purchase[0],
                "time_of_purchase": purchase[1],
                "price": purchase[2],
                "order_ready": purchase[3],
                "order_delivered": purchase[4],
                "delivery_method": purchase[5],
                "address_id": purchase[6],
                "total_amount_payed": purchase[7],
                "tips": purchase[8],
                "discount": purchase[9],
                "customer_id": purchase[10],
                "payment_id": purchase[11]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(purchase_info)

def purchases_per_day():
    db = app.get_db()
    cur = db.cursor()
    try:

        sql = "SELECT purchase_time FROM purchase;"
        cur.execute(sql)
        days = []
        for purchase_time in cur.fetchall():
            sql_how_many_per_day = "SELECT COUNT(*) as total_purchases FROM purchase WHERE purchase_time >= DATE_SUB(%s, INTERVAL 0 DAY);"
            cur.execute(sql_how_many_per_day, (purchase_time.date,))
            total_purchases = cur.fetchone()
            new = {
                "time_of_purchase": purchase_time,
                "total_purchases": total_purchases,
            }
            days.append(new)
        if len(days) <= 0:
            print("No purchases in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(days)

def get_purchases_on_date(date):
    db = app.get_db()
    cur = db.cursor()

    try:
        sql = "SELECT COUNT(*) FROM purchase WHERE DATE(purchase_time)=%s;"
        cur.execute(sql, (date, ))

        count = cur.fetchone()
        if count[0] == 0:
            raise NameError("No purchases on this date")
        else:
            purchases_on_date = {
                "amount_of_purchases_on_"+date: count[0]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return purchases_on_date

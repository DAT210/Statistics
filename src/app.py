"""
DAT210
Statistics: Python/flask app

"""

from flask import Flask, render_template, request, redirect, url_for, session, g, send_from_directory, jsonify
import mysql.connector
import json
import collections

app = Flask(__name__)
app.debug = True  # only for development!

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "root"
app.config["DATABASE_DB"] = "statistics"
app.config["DATABASE_HOST"] = "localhost"

app.secret_key = "secret_key"

# Get connection to db
def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"],
                                              database=app.config["DATABASE_DB"])
    return g._database

# Close db connection
@app.teardown_appcontext
def teardown_db(error):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# Front end client routes and functions
@app.route("/statistics/")
def index():
    return render_template("index.html")

@app.route("/statistics/charts/")
def charts():
    return render_template("charts.html", orders_per_month=orders_per_month(), 
        orders_per_dish=orders_per_dish())

@app.route("/statistics/tables/")
def tables(): 
    return render_template("tables.html", orders=get_all_orders(), customers=get_all_customers(), 
        dishes=get_all_dishes())

def orders_per_month():
    orders = get_all_orders()
    res = {}
    for order in orders:
        curr_month = order["date"].month
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

def orders_per_dish():
    orders = get_all_orders()
    dish_lookup = get_dish_lookup_dict()
    res = {}

    for order in orders:
        curr_dish_id = order["dish_id"]
        if curr_dish_id in res:
            res[curr_dish_id] += 1
        else:
            res[curr_dish_id] = 1
   
    res_names = {}  # New dict with dish name instead of dish id
    for id, count in res.items():
        dish_name = dish_lookup[id]
        res_names[dish_name] = count

    res_names = collections.OrderedDict(sorted(res_names.items()))  # Sort result based on dish name
    return json.dumps(res_names)

def get_all_orders():
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM orders"
        cur.execute(sql)

        orders = []
        for order in cur.fetchall():
            new = {
                "order_id": order[0],
                "time_stamp": str(order[1]),
                "date": order[2],
                "order_type": order[3],
                "customer_id": order[4],
                "dish_id": order[5],
                "delivery": order[6],
                "price": order[7]
            }
            orders.append(new)
        if len(orders) <= 0:
            print("No orders in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return orders

def get_order(order_id):

    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM orders WHERE order_id=%s"
        cur.execute(sql, (order_id, ))

        order = cur.fetchone()
        if order == None:
            raise NameError("This order_id doesn\'t exist in our database")
        else:
            order_info = {
                "order_id": order[0],
                "timestamp": str(order[1]),
                "date": order[2],
                "order_type": order[3],
                "customer_id": order[4],
                "dish_id": order[5],
                "delivery": order[6],
                "price": order[7]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return order_info

def get_all_dishes():
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM dish"
        cur.execute(sql)

        dishes = []
        for dish in cur.fetchall():
            new = {
                "dish_id": dish[0],
                "dish_name": dish[1],
                "price": dish[2]
            }
            dishes.append(new)
        if len(dishes) <= 0:
            print("No dishes in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return dishes

def get_dish(dish_id):
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM dish WHERE dish_id=%s"
        cur.execute(sql, (dish_id, ))
        dish = cur.fetchone()
        if dish == None:
            raise NameError("This dish_id doesn\'t exist in the database")
        else:
            dish_info = {
                "dish_id": dish[0],
                "dish_name": dish[1],
                "price": dish[2]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return dish_info

def get_dish_lookup_dict():
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM dish"
        cur.execute(sql)

        dishes = {}
        for dish in cur.fetchall():
            dish_id, dish_name = dish[0], dish[1]
            dishes[dish_id] = dish_name

        if len(dishes) <= 0:
            print("No dishes in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return dishes

def get_customer(customer_id):
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM customer WHERE customer_id=%s"
        cur.execute(sql, (customer_id, ))

        customer = cur.fetchone()
        if customer == None:
            raise NameError("This customer_id doesn\'t exist in the database")
        else:
            customer_info = {
                "customer_id": customer[0],
                "f_name": customer[1],
                "s_name": customer[2],
                "phone": customer[3],
                "birthdate": customer[4],
                "email": customer[5],
                "c_address": customer[6]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return customer_info

def get_all_customers():
    db = get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM customer"
        cur.execute(sql)

        customers = []
        for customer in cur.fetchall():
            new = {
                "customer_id": customer[0],
                "f_name": customer[1],
                "s_name": customer[2],
                "phone": customer[3],
                "birthdate": customer[4],
                "email": customer[5],
                "c_address": customer[6]
            }
            customers.append(new)
        if len(customers) <= 0:
            print("No dishes in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return customers

# API routes
@app.route("/statistics/orders/")
def orders():
    return "/statistics/orders/"

@app.route("/statistics/orders/<int:order_id>/")
def show_order(order_id):
    order = get_order(order_id)
    return jsonify(order)

@app.route("/statistics/customers/")
def customers():
    return "/statistics/customers/"

@app.route("/statistics/customers/<int:customer_id>/")
def show_customer(customer_id):
    return jsonify(get_customer(customer_id))

@app.route("/statistics/dish/")
def dishes():
    return "/statistics/dish/"

@app.route("/statistics/dish/<int:dish_id>/")
def show_dishes(dish_id):
    return jsonify(get_dish(dish_id))

# Error handlers 
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def bad_request500(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run()

"""
DAT210
Statistics: Python/flask app

"""

from flask import Flask, render_template, request, redirect, url_for, session, g, send_from_directory
import mysql.connector

app = Flask(__name__)
app.debug = True  # only for development!

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "V3lkommen"
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


# Routes for front end client
@app.route("/statistics/")
def index():
    return render_template("index.html")

@app.route("/statistics/charts/")
def charts():
   return render_template("charts.html")

@app.route("/statistics/tables/")
def tables():
    return render_template("tables.html")

# API routes
@app.route("/statistics/orders/")
def orders():
    return "/statistics/orders/"

@app.route("/statistics/orders/<int:order_id>/")
def show_order(order_id):
    order = get_order(order_id)
    return str(order)

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
                "timestamp": order[1],
                "order_type": order[2],
                "customer_id": order[3],
                "dish_id": order[4],
                "delivery": order[5],
                "price": order[6]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return order_info

@app.route("/statistics/customers/")
def customers():
    return "/statistics/customers/"


@app.route("/statistics/customers/<int:customer_id>/")
def show_customer(customer_id):
    customer = get_customer(customer_id)
    return render_template("show_customer.html", customer=customer)
    #return str(customer)

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

@app.route("/statistics/dish/")
def dishes():
    return "/statistics/dish/"

@app.route("/statistics/dish/<int:dish_id>/")
def show_dishes(dish_id):
    dish = get_dish(dish_id)
    return str(dish)

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

# Error handlers 
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def bad_request500(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run()

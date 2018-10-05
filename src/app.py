"""
DAT210
Statistikk API med python/flask

"""

from flask import Flask, render_template, request, redirect, url_for, session, g, send_from_directory
import mysql.connector

app = Flask(__name__)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "V3lkommen"
app.config["DATABASE_DB"] = "statistics"
app.config["DATABASE_HOST"] = "localhost"

app.secret_key = "secret_key"



# Henter statistikk-databasen
def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"],
                                              database=app.config["DATABASE_DB"])
    return g._database

# Lukker databasen
@app.teardown_appcontext
def teardown_db(error):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()




# Rute til dashboard
@app.route("/statistics/dashboard/")
def dashboard():
    return render_template("dashboard.html")

# Rute til charts
@app.route("/statistics/charts/")
def charts():
   return render_template("charts.html")

# Rute til tables
@app.route("/statistics/tables/")
def tables():
    return render_template("tables.html")




# Rute til bestillingsordrene
@app.route("/statistics/orders/")
def orders():
    return "/statistics/orders/"

# Rute til spesifikk bestillingsorder med order_id
@app.route("/statistics/orders/<int:order_id>/")
def show_order(order_id):
    order = get_order(order_id)
    return str(order)

# Funksjon for å hente spesifikk ordre fra databasen og returnere detaljer
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




# Rute til kunder/customers
@app.route("/statistics/customers/")
def customers():
    return "/statistics/customers/"

# Rute til spesifikk kunde med customer id
@app.route("/statistics/customers/<int:customer_id>/")
def show_customer(customer_id):
    customer = get_customer(customer_id)
    return render_template("show_customer.html", customer=customer)
    #return str(customer)

# Funksjon for å hente spesifikk kunde fra databasen og returnere detaljer
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




# Rute til retter/dishes
@app.route("/statistics/dish/")
def dishes():
    return "/statistics/dish/"

# Rute til spesifikk rett med dish id
@app.route("/statistics/dish/<int:dish_id>/")
def show_dishes(dish_id):
    dish = get_dish(dish_id)
    return str(dish)

# Funksjon for å hente spesifikk rett fra databasen og returnere detaljer
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




# Error handler
@app.errorhandler(404)
def bad_request404(error):
    return render_template("404.html"), 404



# Kjører app.py
if __name__ == "__main__":
    app.run(debug=True) # Fjern debug=True senere

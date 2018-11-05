"""
DAT210
Statistics: Python/flask app

"""

from flask import Flask, render_template, request, redirect, url_for, session, g, send_from_directory, jsonify
import mysql.connector
import json
import collections
from statistics_functions import order_functions, course_functions, customer_functions, input_functions


app = Flask(__name__)
app.debug = True  # only for development!

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "root"
app.config["DATABASE_DB"] = "dat210_statistics"
app.config["DATABASE_HOST"] = "localhost"

app.secret_key = "secret_key"

# Get connection to db
def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(
            host=app.config["DATABASE_HOST"],
            user=app.config["DATABASE_USER"],
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
    return render_template("charts.html", orders_per_month=order_functions.orders_per_month(), 
        orders_per_dish=order_functions.courses_sold())

@app.route("/statistics/tables/")
def tables(): 
    return render_template("tables.html", orders=order_functions.get_all_orders(), customers=customer_functions.get_all_customers(), 
        courses=course_functions.get_all_courses())

# API routes
@app.route("/statistics/orders/")
def orders():
    return "/statistics/orders/"

@app.route("/statistics/orders/<int:order_id>/")
def show_order(order_id):
    order = order_functions.get_order(order_id)
    return jsonify(order)

@app.route("/statistics/customers/")
def customers():
    return "/statistics/customers/"

@app.route("/statistics/customers/<int:customer_id>/")
def show_customer(customer_id):
    return jsonify(customer_functions.get_customer(customer_id))

@app.route("/statistics/dish/")
def dishes():
    return "/statistics/dish/"

@app.route("/statistics/dish/<int:course_id>/")
def show_dishes(course_id):
    return jsonify(course_functions.get_course(course_id))

# Input routes

@app.route("/statistics/input") #After testing, set with "methods='POST'"
def input():
    #json_content = request.get_json()
	json_content = json.dumps({"input_type": "new_course", "course_id": "3", "course_name": "navneksempel", "price": "123", "category": "food", "information":"sometext", "ingredient_ids":["5"]})
	if json_content == None:
		return "No json content detected"
	return str(input_functions.input(json_content))

# Error handlers 
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def bad_request500(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run()

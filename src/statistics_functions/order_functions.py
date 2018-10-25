from flask import Flask, render_template, request, redirect, url_for, session, g, send_from_directory, jsonify
import mysql.connector
import json
import collections
import app
import dish_functions

# Includes all order related functions

def get_all_orders():
    db = app.get_db()
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
    dish_lookup = dish_functions.get_dish_lookup_dict()
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


def get_order(order_id):

    db = app.get_db()
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



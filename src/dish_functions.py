from flask import Flask, render_template, request, redirect, url_for, session, g, send_from_directory, jsonify
import mysql.connector
import json
import collections
import app

# Includes all dish related functions

def get_all_dishes():
    db = app.get_db()
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
    db = app.get_db()
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
    db = app.get_db()
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
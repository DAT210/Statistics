from flask import Flask, render_template, request, redirect, url_for, session, g, send_from_directory, jsonify
import mysql.connector
import json
import collections
import app

# Includes all customer related functions

def get_customer(customer_id):
    db = app.get_db()
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
    db = app.get_db()
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
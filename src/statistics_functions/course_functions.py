import mysql.connector
import json
import collections
import app

# Includes all dish related functions

def get_all_courses():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT * FROM course;"
        cur.execute(sql)

        courses = cur.fetchall()
        all_courses = []
        for course in courses:
            new = {
                "course_id": course[0],
                "course_name": course[1],
                "price": course[2],
                "category": course[3],
                "information": course[4]
            }
            all_courses.append(new)
        if len(courses) <= 0:
            print("No courses in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return all_courses # Do not json.dumps() this. Need a python dict in Jinja

def get_course(course_id):
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT course_name, price, category, information FROM course WHERE course_id=%s;"
        cur.execute(sql, (course_id))
        course = cur.fetchone()
        if course == None:
            raise NameError("This dish_id doesn\'t exist in the database")
        else:
            course_info = {
                "course_id": course_id,
                "course_name": course[0],
                "price": course[1],
                "category": course[2],
                "information": course[3]
            }

    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(course_info)

def get_course_lookup_dict():
    db = app.get_db()
    cur = db.cursor()
    try:
        sql = "SELECT course_id, course_name FROM course"
        cur.execute(sql)

        courses = {}
        for course in cur.fetchall():
            course_id, course_name = course[0], course[1]
            courses[course_id] = course_name

        if len(courses) <= 0:
            print("No courses in our database")
    except mysql.connector.Error as err:
        print("Oops, something went wrong:", err)
    finally:
        cur.close()
    return json.dumps(courses)

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
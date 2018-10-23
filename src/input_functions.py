import mysql.connector
import json
import collections

# this will execute a function to input data to DB based
# on the "input_type" field of the POST request
def input(json_content):
    content = json.load(json_content)
    {"completed_order" : completed_order,
    "other_input" : other_input
    # add new funtions for all types of input
    }[content["input_type"]](content)

def completed_order(content):
    return

def other_input(content):
    return
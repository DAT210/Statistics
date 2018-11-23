

![Logo of the project](https://kit8.net/images/thumbnails/700/525/detailed/1/Graph.png)

# Statistics &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)

> Statistics service for restaurant project

## Getting started

A quick introduction of the minimal setup you need to get our web app running.

```shell
python -m pip install Flask
python -m pip install mysql-connector
python app.py
```

Installs required packages and starts the web app local server on http://localhost:5000/  
Current routes starts on http://localhost:5000/statistics/  
You will need to have Python and MySQL installed with a created database.
In the app.py file you will also need to adjust the database configs according to your local database settings e.g. change the password and database name.

## Developing

### Built With

[Docker](https://www.docker.com/get-started)  

[Python](https://www.python.org/), version 3.7

[Flask](http://flask.pocoo.org/), version 1.0.2

[MySQL](https://www.mysql.com/), version 5.7


### API reference
#### Input
All information we collect must be sent to the server via a POST request that includes a json object to the route "/statistics/input".
In this json object, there must be a field with the name "input_type" that expresses what kind of input it is, as the server will
execute a different set of queries based on this field. Depending on this field, other fields must also be specified.
See the current list in the following table (subject to change)(fields are required, but empty values are allowed):

| "input_type" |Required fields|Notes|
|---|---|---|
|"new_customer"|"customer_id", "first_name", "last_name", "email", "phone", "birthdate", "address_id"|Address must already exist in address table|
|"new_booking"|"booking_id", "restaurant_id", "table_id", "booking_date", "booking_length", "no_of_seats", "customer_id"|Customer must be in customer table|
|"new_employee"|"employee_id", "first_name", "last_name", "email", "phone", "birthdate", "address_id", "restaurant_id", "salary", "start_date"|Address and restaurant must exist in their own table|
|"new_course"|"course_id", "course_name", "price", "category", "information", "ingredient_ids"|"ingredient_ids" expects a *list* of ids|
|"new_completed_purchase"|"purchase_id", "purchase_time", "price", "delivery_method", "address_id", "amount", "tips", "discount", "customer_id", "payment_id" "course_ids_with_quantity"| "price" refers to stock price the customer would normally be expected to pay, while "amount" is the total amount payed after discounts and including tips. "course_ids_with_quantity" expects a *list* of *lists*|
|"new_review"|"review_id", "course_id", "review_text", "score"
|"new_ingredient"|"ingredient_id", "ingredient_name", "quantity_in_stock", "allergene_ids_and_names"| "allergene_ids_and_names" expects a *list* of *lists*|
|"new_address"| "address_id", "city", "postcode", "street_name", "street_number", "apartment_number"|
|"new_restaurant"|"restaurant_id", "restaurant_name", "phone", "address_id"|
|"update_order_ready_time"|"purchase_id", "order_ready_time"|When was the preperation of the order finished|  
|"update_delivery_finished_time"|"purchase_id", "order_delivered_time"|When was the delivery of the order finished|
|"update_ingredient_quantity_in_stock"|"ingredient_id", "quantity_in_stock"|Updates table value to correct amount in stock|

#### Get:
Unlike input functions, all get functions have their own route. Start with "statistics/" and append appropriate "get_function" from table above, e.g. "statistics/purchases/99".
Output will be a JSON object containing data from db corresponding to your request.

| "get_function" |Notes|
|---|---|
|purchases|Get all purchases|
|purchases/<int:purchase_id>|Get the purchase with the specified purchase_id|
|purchases/<string:date>|Get amount of purchases on the specific date in the format "YYYY-MM-DD"|
|customers|Get all customers|
|customers/<int:customer_id>|Get the purchase with the specified customer_id|
|courses|Get all courses|
|courses/<int:course_id>|Get the course with the specified course_id|

#### OpenAPI documentation
Find [here](https://github.com/DAT210/Statistics/blob/dev/src/openapi.yaml).

### Setting up dev
If you want to develop this project further, you need to have Python3 and MySQL installed on your machine (as stated in the wuick start guide). If you do not have Python3, easiest way to get it is by installing [Anaconda](https://www.anaconda.com/download). Look at [MySQL's official website](https://dev.mysql.com/doc/refman/8.0/en/installing.html) for guide on how to install if you need.

Next step is to run these commands in cmd or terminal to clone git repo and install needed Python packages.
```shell
git clone https://github.com/DAT210/Statistics.git
python -m pip install Flask
python -m pip install mysql-connector
python -m pip install Faker
```

After everything is installed and ready you need to log in to MySQL environment, create and populate the database.
```shell
mysql -u [username] -p 
source [git repo path]/Statistics/src/db/db_init.sql
exit
python [git repo path]/Statistics/src/db/db_filler.py
```

### Running
After setting up dev environment you can run the app.py file form the src folder.
REMARK: You need to change database configuration in app.py file to your local database config before running.
```shell
python app.py
```
This will run the server as a localhost at the default port number, 5000.


### Deploying / Publishing
Deployment of the code will happen automatically when new versions are pushed to default branch (dev).
An Azure pipeline will then trigger a build pipeline that will push a new image which will be deployed [here](https://dat210statistics.azurewebsites.net).

### Tests
Run these commands on your shell/terminal to run the postman tests which tests the GET and POST functions of our API to see if the routes works as it should.  
You need to have the local web server running. 
To run the tests on your CLI you will need Newman, which is a command line Collection Runner for Postman. Newman is built on Node.js, so make sure your have [Node.js](https://nodejs.org/en/download/) installed as well. Check out this [link](https://www.getpostman.com/docs/v6/postman/collection_runs/command_line_integration_with_newman#options) for some more details on how to run the collection with flags.  
If you don't have Newman another alternative is to download the [Postman](https://www.getpostman.com/apps) client, export the "collection.json" file and run the collection there.

```shell
cd Statistics/src/
python app.py
newman run RestaurantFunctionsTests.postman_collection.json

If you don't have newman installed, the easiest way to install it is with npm which comes with Node.js:
npm install -g newman

When running the tests on your shell, your output should look like this:
$ newman run RestaurantFunctionsTests.postman_collection.json
newman

Restaurant Functions Tests

□ get_all
└ get_all_customers
  GET localhost:5000/statistics/customers/ [200 OK, 42.19KB, 624ms]
  √  Status code is 200
  √  Response time is acceptable: 624ms
  √  Content-Type header is set as application/json
  √  Customers ID is present
  √  Customers first name is present
  √  Customers last name is present
  √  Customers email is present
  √  Customers phone is present
  √  Customers birthdate is present
  √  Customers address is present

└ get_all_courses
  GET localhost:5000/statistics/courses/ [200 OK, 2.75KB, 509ms]
  √  Status code is 200
  √  Response time is acceptable: 509ms
  √  Content-Type header is set as application/json
  √  Course ID is present
  √  Course name is present
  √  Course price is present
  √  Course category is present
  √  Course information is present

└ get_all_purchases
  GET localhost:5000/statistics/purchases/ [200 OK, 198.55KB, 571ms]
  √  Status code is 200
  √  Response time is acceptable: 571ms
  √  Content-Type header is set as application/json
  √  Purchase ID is present
  √  Time of purchase is present
  √  Purchase price is present
  √  Purchase order ready is present
  √  Purchase order delivered is present
  √  Purchase delivery method is present
  √  Purchase address ID is present
  √  Purchase total price is present
  √  Purchase tips is present
  √  Purchase discount is present
  √  Purchase customer ID is present
  √  Purchase payment ID is present

etc.
```

### Database design
![Database design](https://i.imgur.com/KKPJ0SU.png)

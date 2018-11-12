

![Logo of the project](https://kit8.net/images/thumbnails/700/525/detailed/1/Graph.png)

# Statistics &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
> Statistics service for restaurant project

Statistics service that will store and serve statisitcs for the restaurant business.

## Installing / Getting started ##TODO

A quick introduction of the minimal setup you need to get our web app running.

```shell
python -m pip install Flask
python -m pip install mysql-connector
python app.py
```

Installs required packages and starts the web app local server on http://localhost:5000/  
Current routes starts on http://localhost:5000/statistics/  
You will need to have Python installed. In the app.py file you will also need to adjust the database configs according to your local database settings e.g. change the password and database name.

## Developing

### Built With
Python/Flask
MySQL

### Prerequisites
[Docker](https://www.docker.com/get-started)  
[Python](https://www.python.org/)  
[Flask](http://flask.pocoo.org/)  
[MySQL](https://www.mysql.com/)


## API:
### Input
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

### Get:
Unlike input functions, all get functions have their own path. Specify statistics/ and then append appropriate "get_function" from table above, e.g. statistics/purchases/99.

| "get_function" |Notes|
|---|---|
|purchases|Get all purchases|
|purchases/<int:purchase_id>|Get the purchase with the specified purchase_id|
|purchases/<string:date>|Get the purchase with the specified purchase_id|
|customers|Get all customers|
|customers/<int:customer_id>|Get the purchase with the specified customer_id|
|courses|Get all courses|
|courses/<int:course_id>|Get the course with the specified coures_id|

### OpenAPI documentation
https://github.com/DAT210/Statistics/blob/dev/src/openapi.yaml

## Setting up dev
Here's a brief intro about what a developer must do in order to start developing
the project further, assuming you have Python3 already installed. If not, easiest way to get Python3 is by installing the Anaconda distribution (https://www.anaconda.com/download). You also need to hav MySQL installed on your computer. Look at MySQL's official website for guide on how to install (https://dev.mysql.com/doc/refman/8.0/en/installing.html).

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

## Running

After setting up dev environment you can run the app.py file form the src folder.
REMARK: You need to change database configuration in app.py file to your local database config before running.
```shell
python app.py
```
This will run the server and you will be able to use the services as intended.

### Deploying / Publishing ##TODO
Give instructions on how to build and release a new version
In case there's some step you have to take that publishes this project to a
server, this is the right time to state it.

```shell
packagemanager deploy your-project -s server.com -u username -p password
```

And again you'd need to tell what the previous code actually does.

## Versioning ##TODO
We can maybe use [SemVer](http://semver.org/) for versioning. For the versions available, see the [link to tags on this repository](/tags).


## Configuration ##TODO
Here you should write what are all of the configurations a user can enter when
using the project.

## Tests ##TODO
Run these commands on a shell/terminal to run the postman tests which tests the GET and POST functions of our API to see if the routes works as it should.  
You need to have the local web server running.  
If you don't have Node.js another alternative is to install Postman from https://www.getpostman.com/apps and export the json file and run the collection there.

```shell
cd Statistics/src/
python app.py
newman run RestaurantFunctionsTest.json

If you don't have newman installed, the easiest way to install it is with npm which comes with Node.js:
npm install -g newman
```

## Style guide ##TODO
Explain your code style and show how to check it.

## Database design
![Database design](https://i.imgur.com/KKPJ0SU.png)

## Licensing ##TODO
State what the license is and how to find the text version of the license.

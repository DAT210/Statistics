

![Logo of the project](https://kit8.net/images/thumbnails/700/525/detailed/1/Graph.png)

# Statistics &middot; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
> Statistics service for restaurant project

Statistics service that will store and serve statisitcs for the restaurant business.

## Installing / Getting started ##TODO

A quick introduction of the minimal setup you need to get our web app running.

```shell
python -m pip install Flask
python -m pip install mysql-connector-python
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


## How the server handles incoming input to be put in the database:
All information we collect must be sent to the server via a POST request that includes a json object to the route "/statistics/input".
In this json object, there must be a field with the name "input_type" that expresses what kind of input it is, as the server will
execute a different set of queries based on this field. Depending on this field, other fields must also be specified.
See the current list in the following table (subject to change)(fields are required, but empty values are allowed):

| "input_type" |Required fields|Notes|
|---|---|---|
|"new_customer"|"city", "postcode", "street_name", "street_number", "apartment_number", "first_name", "last_name", "email", "phone", "birthdate", "address_id"||
|"new_booking"|"first_name", "last_name", "restaurant_name", "table_id", "booking_date", "booking_length", "no_of_seats"|
|"new_employee"|"restaurant_name", "city", "postcode", "street_name", "street_number", "apartment_number", "first_name", "last_name", "email", "phone", "birthdate", "salary", "start_date"|
|"new_course"|"course_id", "course_name", "price", "category", "information", "ingredient_ids"|"ingredient_ids" expects a *list* of ids|
|"new_completed_purchase"|"purchase_id", "purchase_time", "price", "delivery_method", "address_id", "amount", "tips", "discount", "customer_id", "payment_id" "course_ids_with_quantity"| "price" refers to stock price the customer would normally be expected to pay, while "amount" is the total amount payed after discounts and including tips. "course_ids_with_quantity" expects a *list* of *touples*|
|"new_review"|"review_id", "course_id", "review_text", "score"
|"new_ingredient"|"ingredient_id", "ingredient_name", "allergene_ids_and_names"| "allergene_ids_and_names" expects a *list* of *touples*|
|"update_order_ready_time"|"purchase_id", "order_ready_time"|When was the preperation of the order finished|  
|"update_delivery_finished_time"|"purchase_id", "order_delivered_time"|When was the delivery of the order finished|
|"new_address"| "city", "postcode", "street_name", "street_number", "apartment_number"|
|"new_restaurant"|"restaurant_id", "restaurant_name", "phone", "address_id"|






### Setting up Dev ##TODO

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
mkdir MyProjectFolder
cd MyProjectFolder
git clone https://github.com/DAT210/Statistics.git
python -m pip install Flask
python -m pip install mysql-connector-python
```

And state what happens step-by-step. If there is any virtual environment, local server or database feeder needed, explain here.

### Building ##TODO

If your project needs some additional steps for the developer to build the
project after some code changes, state them here. for example:

```shell
./configure
make
make install
```

Here again you should state what actually happens when the code above gets
executed.

### Deploying / Publishing ##TODO
give instructions on how to build and release a new version
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

In app.py file change database configs to your local database config.

## Tests ##TODO

Describe and show how to run the tests with code examples.
Explain what these tests test and why.

```shell
Give an example
```

## Style guide ##TODO

Explain your code style and show how to check it.

## Api Reference ##TODO

If the api is external, link to api documentation. If not describe your api including authentication methods as well as explaining all the endpoints with their required parameters.


## Database ##TODO

Explaining what database (and version) has been used. Provide download links.
Documents your database design and schemas, relations etc... 

## Licensing ##TODO

State what the license is and how to find the text version of the license.

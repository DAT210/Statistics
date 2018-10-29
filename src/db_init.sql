# Statistics DB init 
# Tables for events, discounts, logistics and internal systems not yet implemented!

DROP DATABASE IF EXISTS dat210_statistics;
CREATE DATABASE dat210_statistics CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;	#Setting db charset to UTF-8	
SET default_storage_engine=INNODB;	
USE dat210_statistics;

CREATE TABLE address(
	address_id integer,
    city varchar(128), 
    postcode integer, 
    street_name varchar(128),
    street_number integer,
    apartment_number integer,
	PRIMARY KEY (address_id)
);
CREATE TABLE customer(
	customer_id integer,
	first_name varchar(128), 
    last_name varchar(128), 
    email varchar(128),
    phone integer,
    birthdate date,
    address_id integer,
	PRIMARY KEY (customer_id),
	FOREIGN KEY (address_id) REFERENCES address(address_id)
);
CREATE TABLE restaurant(
	restaurant_id integer,
    restaurant_name varchar(128), 
    phone integer, 
    address_id integer, 
	PRIMARY KEY (restaurant_id),
	FOREIGN KEY (address_id) REFERENCES address(address_id)
);
CREATE TABLE booking(
	booking_id integer,
    restaurant_id integer, 
    table_id integer, 
    booking_date date, 
    booking_length integer, 
    no_of_seats integer,
    customer_id integer,
	PRIMARY KEY (booking_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
	FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id)
);
CREATE TABLE employee(
	employee_id integer,
    first_name varchar(128), 
    last_name varchar(128), 
    email varchar(128),
    phone integer,
    birthdate date,
    address_id integer,
    restaurant_id integer,
    salary double,
    start_date date,
    PRIMARY KEY (employee_id),
    FOREIGN KEY (address_id) REFERENCES address(address_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id)
);
CREATE TABLE payment(
	payment_id integer,
    order_id integer,
    amount double,
    tips double,
    paid_at datetime,
    discount double,
    PRIMARY KEY(payment_id)
);
CREATE TABLE purchase(
	purchase_id integer,
    purchase_time datetime,
    price double,
	order_ready datetime,
    delivery_method varchar(128),
	address_id integer,
    order_delivered datetime,
    customer_id integer,
    payment_id integer,
    PRIMARY KEY (purchase_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (payment_id) REFERENCES payment(payment_id)
);
CREATE TABLE course(
	course_id integer,
    course_name varchar(128),
	price double,
    category varchar(128),
    information text,
    PRIMARY KEY(course_id)
);
CREATE TABLE course_in_purchase(
	course_id integer,
    purchase_id integer,
	PRIMARY KEY (course_id, purchase_id),
	FOREIGN KEY (course_id) REFERENCES course(course_id),
	FOREIGN KEY (purchase_id) REFERENCES purchase(purchase_id)
);
CREATE TABLE ingredient(
	ingredient_id integer,
    ingredient_name varchar(128),
	PRIMARY KEY (ingredient_id)
);
CREATE TABLE ingredient_in_course(
	course_id integer,
    ingredient_id integer,
	PRIMARY KEY (course_id,  ingredient_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id),
	FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id)
);
CREATE TABLE allergene(
	allergene_id integer,
    allergene_name varchar(128),
	PRIMARY KEY (allergene_id)
);
CREATE TABLE allergene_in_ingredient(
	ingredient_id integer,
    allergene_id integer,
	PRIMARY KEY (ingredient_id,  allergene_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id),
	FOREIGN KEY (allergene_id) REFERENCES allergene(allergene_id)
);
CREATE TABLE review(
	review_id integer,
    course_id integer,
    review_text text,
    score integer,
	PRIMARY KEY (review_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);


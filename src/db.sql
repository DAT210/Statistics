
CREATE DATABASE IF NOT EXISTS statistics;
USE statistics;

CREATE TABLE customer(
  customer_id INT(9) AUTO_INCREMENT,
  f_name VARCHAR(20),
  s_name VARCHAR(30),
  phone INTEGER,
  birthdate DATE,
  email VARCHAR(50),
  c_address VARCHAR(100),
  PRIMARY KEY(customer_id)
)ENGINE=InnoDB;

CREATE TABLE dish(
    dish_id INT(9) AUTO_INCREMENT,
    dish_name VARCHAR(50),
    price INT(9),
    PRIMARY KEY(dish_id)
    )ENGINE=InnoDB;

CREATE TABLE orders(
    order_id INT(9) AUTO_INCREMENT,
    time_stamp DATETIME,
    order_type VARCHAR(20),
    customer_id INT(9),
    dish_id INT(9),
    delivery VARCHAR(32) DEFAULT NULL,
    price INT(9), DEFAULT NULL,
    PRIMARY KEY(order_id),
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY(dish_id) REFERENCES dish(dish_id)
    )ENGINE=InnoDB;

INSERT INTO customer(f_name, s_name, phone, birthdate, email, c_address)
VALUES('Ola', 'Nordmann', 12345678, '1945-04-09', 'N/A', 'Slottsplassen 1'),
      ('Trude', 'Dali', 324324278, '1914-05-07', 'dali@gmail.com', 'Bryggen 51'),
      ('Kari', 'Sjeldbrei', 322342678, '2014-06-06', 'sugarbaby@hacks.co', 'Langata 52'),
      ('Sara', 'Wathne', 32455688, '2013-08-23', 'swathne92@hotmail.com', 'Fargegaten 52');

INSERT INTO dish(dish_name, price)
VALUES("Chicken Tikka Masala", 150),
      ("Baguette, Ost+Skinke", 80),
      ("Boeuf Bourgieonon", 200),
      ("Cheeseburger", 99);

INSERT INTO orders(time_stamp, order_type, customer_id, dish_id)
VALUES(NOW(), "takeaway", 2, 1),
      (CURRENT_TIMESTAMP(), "inhouse", 3, 4),
      (CURRENT_TIMESTAMP(), "inhouse", 3, 2),
      (CURRENT_TIMESTAMP(), "inhouse", 3, 1),
      (NOW(), "takeaway", 4, 3);

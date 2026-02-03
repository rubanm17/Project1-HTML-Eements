DROP IF TABLE EXISTS salesman;
CREATE TABLE IF NOT EXISTS salesman (
    salesman_id TEXT PRIMARY KEY,
    name TEXT ,
    city TEXT ,
    commission TEXT
);

INERT INTO salesman (salesman_id, name, city, commission) VALUES
('5001', 'James hoog', 'New York', '0.15'),
('5002', 'Nail kite', 'Paris', '0.13'),
('5005', 'Pit Alex', 'London', '0.11'),
('5006', 'Mc Lyon', 'Paris', '0.14'),
('5007', 'Paul Adam', 'Rome', '0.13'),
('5003', 'Lauson Hen', 'San Jose', '0.12');

CREATE TABLE IF NOT EXISTS customer (
    cust_id TEXT ,
    cust_name TEXT PRIMARY KEY,
    city TEXT ,
    grade TEXT ,
    salesman_id TEXT;
);

INSERT INTO customer (cust_id, cust_name, city, grade, salesman_id) VALUES
('3002', 'Nick Rimando', 'New York', '100', '5001'),
('3007', 'Brad Davis', 'New York', '200', '5001'),
('3005', 'Graham Zusi', 'California', '200', '5002'),
('3008', 'Julian Green', 'London', '300', '5002'),
('3004', 'Fabian Johnson', 'Paris', '300', '5006'),
('3009', 'Geoff Cameron', 'Berlin', '100', '5003'),
('3003', 'Jozy altidor', 'Moscow', '200', '5007'),
('3001', 'Brad Guzan', 'London', '', '5005');

CREATE TABLE IF NOT EXISTS orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt TEXT ,
    ord_date TEXT ,
    customer_id TEXT ,
    salesman_id TEXT
);

INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('70001', '150.5', '2012-10-05', '3005', '5002'),
('70009', '270.65', '2012-09-10', '3001', '5001'),
('70002', '65.26', '2012-10-05', '3002', '5003'),
('70004', '110.5', '2012-08-17', '3009', '5007'),
('70007', '948.5', '2012-09-10', '3005', '5005'),
('70005', '2400.6', '2012-07-27', '3007', '5006');

SELECT customer.cust_id,salesman.name,salesman.city
FROM customer
JOIN salesman ON customer.city = salesman.city;

SELECT customer.cust_ name,Salesman.name
FROM customer
JOIN salesman ON customer.salesman_id = salesman.salesman_id;

SELECT orders.ord_no,customer.cust_name,orders.cutomer_id,orders.salesman_id
FROM custumors
JOIN customers ON orders.customer_id = customer.customer_id
JOIN Salesman ON orders.salesman_id = salesman.salesman_id
WHERE customer.city <> salesman.city;

SELECT orders.ord_no,customer.cust_name
FROM orders
JOIN customer ON orders.customer_id = customer.customer_id;

SELECT customer.cust_name AS "Customer" , customer.grade AS "Grade"
FROM orders
JOIN salesman ON orders.salesman_id = salesman.salesman_id
JOIN customer ON orders.customer_id = customer.customer_id
WHERE customer.grade IS NOT NULL;

SELECT customer.cust_name AS "Customer",
customer.city AS "City",
salesman.name AS "Salesman",
salesman.commission
FROM customers
JOIN salesman ON customer.salesman_id = salesman.salesman_id
WHERE salesman.commission BETWEEN 0.12 AND 0.14;

SELECT orders.ord_no,customer.cust_name,salesman.commission AS "Commission%",
orders.purch_amt * saleman.commission AS "Commission"
FROM orders
JOIN salesman ON orders.salesman_id = salesman.salesman_id
JOIN customer ON orders.customer_id = customer.customer_id
WHERE Customer.grade >= 200;

/* SELECT * 
FROM customer
JOIN Orders ON customer.customer_id = orders.customer_id
WHERE orders.ord_no IS NOT NULL; */
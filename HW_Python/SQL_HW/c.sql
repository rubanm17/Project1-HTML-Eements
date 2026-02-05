DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Sales;

CREATE TABLE IF NOT EXISTS Sales(
  salesman_id TEXT PRIMARY KEY,
  name TEXT,
  city TEXT,
  commission TEXT
);

INSERT INTO Sales (salesman_id, name, city, commission)
VALUES 
    ('101', 'John Doe', 'New York', '0.15'),
    ('102', 'Jane Smith', 'Los Angeles', '0.12'),
    ('103', 'Mike Brown', 'Chicago', '0.10'),
    ('104', 'Sarah White', 'Houston', '0.14'),
    ('105', 'Robert Green', 'Seattle', '0.11'),
    ('106', 'Lisa Johnson', 'Miami', '0.13'),
    ('107', 'David Wilson', 'Denver', '0.16');

CREATE TABLE IF NOT EXISTS Customer (
    customer_id TEXT PRIMARY KEY,
    cust_name TEXT NOT NULL,
    city TEXT,
    grade INTEGER,
    salesman_id TEXT
);

INSERT INTO Customer (customer_id, cust_name, city, grade, salesman_id)
VALUES 
('10', 'PREETHI', 'BANGALORE', 1, '101'),
('11', 'JOHN', 'NEW YORK', 2, '102'),
('12', 'LUCKY', 'MUMBAI', 2, '103'),
('13', 'MARK', 'BANGALORE', 3, '104'),
('14', 'DAVID', 'MYSORE', 1, '105'),
('15', 'SMITH', 'DELHI', 3, '106'),
('16', 'HARSHA', 'HYDERABAD', 2, '107');

CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purchase_amt TEXT,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
);

INSERT INTO Orders (ord_no, purchase_amt, ord_date, customer_id, salesman_id)
VALUES 
('101', '1500.50', '2025-01-10', '10', '101'),
('102', '250.00', '2025-01-11', '11', '102'),
('103', '75.20', '2025-01-11', '12', '103'),
('104', '3000.00', '2025-01-12', '13', '104'),
('105', '500.00', '2025-01-13', '14', '105');

-- Queries

-- Matching customers and salesmen by city
SELECT Customer.cust_name, Sales.name, Sales.city
FROM Customer
JOIN Sales ON Customer.city = Sales.city;

-- Linking customers to their salesmen
SELECT Customer.cust_name, Sales.name
FROM Customer
JOIN Sales ON Customer.salesman_id = Sales.salesman_id;

-- Fetching orders where customer's city does not match salesman's city
SELECT Orders.ord_no, Customer.cust_name, Orders.customer_id, Orders.salesman_id
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Sales ON Orders.salesman_id = Sales.salesman_id
WHERE Customer.city <> Sales.city;

-- Fetching all orders with customer names
SELECT Orders.ord_no, Customer.cust_name
FROM Orders
JOIN Customer ON Orders.customer_id = Customer.customer_id;

-- Customers with grades
SELECT Customer.cust_name AS "Customer", Customer.grade AS "Grade"
FROM Orders
JOIN Sales ON Orders.salesman_id = Sales.salesman_id
JOIN Customer ON Orders.customer_id = Customer.customer_id
WHERE Customer.grade IS NOT NULL;

-- Customers with salesmen where commission is between 0.12 and 0.14
SELECT Customer.cust_name AS "Customer",
Customer.city AS "City",
Sales.name AS "Salesman",
Sales.commission
FROM Customer
JOIN Sales ON Customer.salesman_id = Sales.salesman_id
WHERE Sales.commission BETWEEN 0.12 AND 0.14;

-- Calculating commissions for orders where customer grade is 200 or more
SELECT Orders.ord_no, Customer.cust_name, Sales.commission AS "Commission%",
Orders.purchase_amt * Sales.commission AS "Commission"
FROM Orders
JOIN Sales ON Orders.salesman_id = Sales.salesman_id
JOIN Customer ON Orders.customer_id = Customer.customer_id
WHERE Customer.grade >= 200;

-- Orders on a specific date
SELECT *
FROM Customer
JOIN Orders ON Customer.customer_id = Orders.customer_id
WHERE Orders.ord_date = '2025-01-10';
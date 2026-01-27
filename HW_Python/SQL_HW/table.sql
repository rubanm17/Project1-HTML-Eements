CREATE TABLE If NOT EXISTS customers (
    Name TEXT,
    COUNTRY TEXT,
    City TEXT,
    AGE TEXT,
    Grade INTEGER
);

INSERT INTO customers (Name, COUNTRY, City, AGE, Grade) VALUES
('John ', 'USA', 'New York', '30', 120),
('Smith', 'Canada', 'Toronto', '25', 95),
('Sam ', 'USA', 'Los Angeles', '28', 110),
('Lisa', 'UK', 'London', '32', 85),
('Tom ', 'USA', 'New York', '40', 130);

SELECT NAME
FROM customers
WHERE Grade =
(SELECT MAX(Grade) FROM customers);
SELECT AGE
FROM customers
WHERE AGE =
(SELECT MIN(AGE) FROM customers);

SELECT * FROM customers WHERE COUNTRY = 'USA';

SELECT * FROM customers WHERE COUNTRY = 'USA' AND AGE BETWEEN 10 AND 30;

SELECT * FROM customers WHERE NAME LIKE 's%';
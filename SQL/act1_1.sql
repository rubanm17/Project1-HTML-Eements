CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    commission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, commission) VALUES
('5001', 'James hoog', 'Ladak', 0.15),
('5002', 'Nail knite', 'Paris', 0.13),
('5003', 'Pit alex', 'London', 0.11),
('5004', 'Mc Lyon', 'Paris', 0.14),
('5005', 'Tout Weyn', 'Athens', 0.12);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders (
    Ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    Ord_date TEXT,
    Customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO Orders (Ord_no, purch_amt, Ord_date, Customer_id, Salesman_id) VALUES
('70001', 150.5, '2023-01-10', '3001', '5001'),
('70009', 270.65, '2023-01-15', '3002', '5002'),
('70002', 65.26, '2023-01-20', '3001', '5001'),
('70004', 110.5, '2023-01-25', '3003', '5003'),
('70007', 948.5, '2023-01-30', '3004', '5004');

SELECT * FROM Orders;

SELECT name, commission FROM Salesman;
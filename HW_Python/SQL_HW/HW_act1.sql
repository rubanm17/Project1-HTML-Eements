CREATE TABLE employee (
    ENO TEXT Primary Key,
    ENAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO employee (ENO, ENAME, STATUS, CITY) VALUES
('E1', 'Smith', 20, 'London'),
('E2', 'Jones', 10, 'Paris'),
('E3', 'Blake', 30, 'Paris'),
('E4', 'Clark', 20, 'London'),
('E5', 'Adams', 30, 'Athens');

SELECT * FROM employee;
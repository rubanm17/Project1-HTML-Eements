CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT,
    Category TEXT,
    Price TEXT,
    StockQuantity INTEGER NOT NULL
);

INSERT INTO Products (ProductID, ProductName, Category, Price, StockQuantity) VALUES
(1, 'Laptop', 'Electronics', '1200.00', 50),
(2, 'T-Shirt', 'Apparel', '19.99', 200),
(3, 'Coffee Maker', 'Home Appliances', '85.50', 75),
(4, 'Notebook', 'Office Supplies', '4.99', 500),
(5, 'Headphones', 'Electronics', '150.00', 120);

SELECT COUNT(ProductID) AS PRODUCT_COUNT
FROM Products;

SELECT AVG(Price) AS AVERAGE_PRICE
FROM Products;

SELECT SUM(Price) AS TOTAL_PRICE
FROM Products;
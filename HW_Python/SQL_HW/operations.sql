-- Create the table
CREATE TABLE IF NOT EXISTS nomnom (
    Name TEXT,
    NEIGHBOURHOOD TEXT,
    CUISINE TEXT,
    REVIEW REAL,
    PRICE TEXT,
    HEALTH TEXT
);

-- Insert sample data
INSERT INTO nomnom (Name, NEIGHBOURHOOD, CUISINE, REVIEW, PRICE, HEALTH) VALUES
('Pasta Palace', 'Little Italy', 'Italian', 4.5, '$$', 'A'),
('Sushi Spot', 'Downtown', 'Japanese', 4.8, '$$$', 'A+'),
('Burger Joint', 'Midtown', 'American', 3.9, '$', 'B'),
('Taco Town', 'West End', 'Mexican', 4.2, '$', 'A'),
('Curry Corner', 'Downtown', 'Indian', 4.6, '$$', 'A-'),
('The Green Fork', 'Downtown', 'Healthy', 4.8, '$$', 'A+'),
('Green Leaf', 'Downtown', 'Salad', 4.9, '$$', 'A+'),
('The Curry House', 'Brooklyn', 'Indian', 4.3, '$$', 'B+'),
('Pasta Paradise', 'Little Italy', 'Italian', 4.6, '$$$', 'B'),
('Pizza Shack', 'Brooklyn', 'Pizza', 3.8, '$', 'C+'),
('Healthy Bowls', 'Downtown', 'Vegan', 4.7, '$$', 'A'),
('Sugar Rush', 'Midtown', 'Bakery', 4.2, '$', 'D+');

SELECT * FROM nomnom ;

SELECT DISTINCT NEIGHBOURHOOD FROM nomnom;

SELECT DISTINCT CUISINE FROM nomnom;

SELECT * FROM nomnom WHERE CUISINE = 'Chinese';

SELECT * FROM nomnom WHERE REVIEW >= 4.0;

SELECT * FROM nomnom WHERE CUISINE = 'Italian' AND PRICE = '$$$';

SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';

SELECT * FROM nomnom WHERE NEIGHBOURHOOD IN ('Midtown', 'Downtown','Chinatown');

SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;
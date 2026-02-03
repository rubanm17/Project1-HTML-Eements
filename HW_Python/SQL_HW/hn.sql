DROP TABLE IF EXISTS hacker_news;
CREATE TABLE IF NOT EXISTS hacker_news (
    date DATE,
    info TEXT
);

INSERT INTO hacker_news (date, info) VALUES
('2026-01-15', 'Hacker group leaks sensitive government files'),
('2026-01-18', 'Global markets fall after economic slowdown fears'),
('2026-01-20', 'New AI system passes complex reasoning tests'),
('2026-01-22', 'Cybersecurity firm stops massive ransomware attack'),
('2026-01-25', 'Global climate summit reaches historic agreement'),
('2026-01-27', 'Hacker arrested for major banking system breach'),
('2026-01-29', 'Tech giant launches new quantum computing chip'),
('2026-02-01', 'International space mission successfully lands on Mars'),
('2026-02-03', 'Data privacy laws tightened across several countries'),
('2026-02-05', 'Startup disrupts global logistics with AI automation'),
('2026-02-07', 'Ethical hacker discovers flaw in popular mobile app'),
('2026-02-09', 'World leaders discuss cybersecurity threats'),
('2026-02-11', 'Breakthrough in renewable energy storage announced'),
('2026-02-13', 'Major social media platform hit by cyber attack'),
('2026-02-15', 'Global education initiative brings free online courses');

SELECT * 
FROM hacker_news
ORDER BY date DESC;

SELECT *
FROM hacker_news
WHERE info LIKE '%hacker%';
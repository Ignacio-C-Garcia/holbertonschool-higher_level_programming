-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- SELECT city, value FROM temperatures GROUP BY city ORDER BY value;
SELECT city, AVG(value) as avg_temp from temperatures GROUP BY city ORDER BY avg_temp DESC;


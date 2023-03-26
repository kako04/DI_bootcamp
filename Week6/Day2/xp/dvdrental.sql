-- select * from customer

-- SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- SELECT DISTINCT create_date FROM customer;

-- SELECT * FROM customer ORDER BY first_name DESC;

-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

-- SELECT a.address, a.phone 
-- FROM address a 
-- JOIN city c ON a.city_id = c.city_id 
-- JOIN country co ON c.country_id = co.country_id 
-- WHERE co.country = 'United States' AND a.district = 'Texas';

-- SELECT * FROM film WHERE film_id IN (15, 150);

-- SELECT film_id, title, description, length, rental_rate 
-- FROM film 
-- WHERE title = 'your favorite movie';

-- SELECT film_id, title, description, length, rental_rate 
-- FROM film 
-- WHERE title LIKE 'your favorite movie%';

-- SELECT title, rental_rate 
-- FROM film 
-- ORDER BY rental_rate ASC 
-- LIMIT 10;

-- SELECT title, rental_rate 
-- FROM (
--   SELECT title, rental_rate, ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS row_num 
--   FROM film
-- ) AS subquery 
-- WHERE row_num BETWEEN 11 AND 20;

-- SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date 
-- FROM customer c 
-- JOIN payment p ON c.customer_id = p.customer_id 
-- ORDER BY c.customer_id ASC;

-- SELECT * FROM film 
-- WHERE film_id NOT IN 
--   (SELECT DISTINCT film_id FROM inventory);

-- SELECT city, country 
-- FROM city 
-- JOIN country ON city.country_id = country.country_id;


-- UPDATE film
-- SET language_id = 1
-- WHERE film_id IN (1, 2, 3);

-- SELECT
--   tc.table_name, 
--   kcu.column_name, 
--   ccu.table_name AS foreign_table_name,
--   ccu.column_name AS foreign_column_name 
-- FROM 
--   information_schema.table_constraints AS tc 
--   JOIN information_schema.key_column_usage AS kcu
--     ON tc.constraint_name = kcu.constraint_name
--   JOIN information_schema.constraint_column_usage AS ccu
--     ON ccu.constraint_name = tc.constraint_name
-- WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='customer';

-- DROP TABLE customer_review;

-- SELECT COUNT(*) 
-- FROM rental 
-- WHERE return_date IS NULL;

-- SELECT f.title, p.amount
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- WHERE r.return_date IS NULL
-- ORDER BY p.amount DESC
-- LIMIT 30;


-- SELECT f.title 
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE f.description LIKE '%sumo wrestler%' AND a.first_name = 'Penelope' AND a.last_name = 'Monroe';

-- SELECT f.title 
-- FROM film f
-- WHERE f.length < 60 AND f.rating = 'R';

-- SELECT f.title 
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND p.amount > 4 AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- SELECT f.title 
-- FROM film f

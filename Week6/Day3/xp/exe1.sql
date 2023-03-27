-- SELECT name FROM language;

-- SELECT f.title, f.description, l.name 
-- FROM film f 
-- LEFT JOIN language l ON f.language_id = l.language_id;

-- SELECT f.title, f.description, l.name 
-- FROM language l 
-- LEFT JOIN film f ON l.language_id = f.language_id;


-- CREATE TABLE new_film (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (name) VALUES ('The Shawshank Redemption'), ('The Godfather'), ('The Dark Knight');

-- 4
-- CREATE TABLE customer_review (
--   review_id SERIAL PRIMARY KEY,
--   film_id INT NOT NULL,
--   language_id INT NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   score INT NOT NULL,
--   review_text TEXT NOT NULL,
--   last_update TIMESTAMP DEFAULT NOW(),
--   CONSTRAINT fk_film
--     FOREIGN KEY (film_id)
--     REFERENCES new_film(id)
--     ON DELETE CASCADE,
--   CONSTRAINT fk_language
--     FOREIGN KEY (language_id)
--     REFERENCES language(language_id)
--     ON DELETE CASCADE
-- );

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text) 
-- VALUES (1, 1, 'Amazing movie!', 9, 'I loved this movie! It had a great story and amazing performances.'),
--        (2, 2, 'A cinematic masterpiece', 10, 'The Godfather is an incredible movie that everyone should see.');

-- 5 
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (1, 1, 'Great movie!', 9, 'I really enjoyed this film. The acting was superb and the storyline kept me engaged throughout.'),
--        (2, 2, 'One of the best!', 10, 'The Godfather is an all-time classic. The acting, writing, and direction are all top-notch.');


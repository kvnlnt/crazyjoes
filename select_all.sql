SELECT 
        film.title, 
        film.release_year, 
        film.rating, 
        actor.first_name, 
        actor.last_name,
        category.name
FROM 
        film, film_actor, actor, category, film_category
WHERE 
        film.film_id = film_actor.film_id AND
        actor.actor_id = film_actor.actor_id AND
        film.film_id = film_category.film_id AND
        film_category.category_id = category.category_id
ORDER BY film.film_id;

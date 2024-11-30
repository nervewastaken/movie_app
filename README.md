API Documentation for Movie Management System

Overview

This API provides functionality for managing movies, genres, actors, and related data. The API supports CRUD operations and advanced querying capabilities for movies and associated entities.

Movies Endpoints

GET /movies

	•	Description: Fetch all movies with optional filters like actor and director.

POST /movies

	•	Description: Add a new movie to the database.

GET /movies/<int:movie_id>

	•	Description: Fetch details of a single movie by its ID.

PUT /movies/<int:movie_id>

	•	Description: Update details of an existing movie by its ID.

POST /movies/<int:movie_id>/actors

	•	Description: Map one or more actors to a movie by its ID.

GET /movies-by-genre/<string:genre_name>

	•	Description: Fetch all movies belonging to a specific genre.

GET /movies-by-profit

	•	Description: Fetch movies with profits greater than a specified value. Requires a query parameter ?min_profit=<value>.

Actors Endpoints

POST /actors

	•	Description: Add a new actor to the database.

DELETE /actors/<int:actor_id>

	•	Description: Delete an actor if they are not associated with any movies.

GET /actors/<int:actor_id>

	•	Description: Fetch details of a specific actor by their ID.

GET /actors-with-movies

	•	Description: Fetch all actors along with the movies they have acted in.

Genres Endpoints

GET /genres

	•	Description: Fetch all genres available in the database.

POST /genres

	•	Description: Add a new genre to the database.

POST /genres/movies/<int:movie_id>

	•	Description: Assign one or more genres to a movie by its ID.

DELETE /genres/<int:genre_id>

	•	Description: Delete a genre if it is not associated with any movies.

Additional Information

	•	Ensure to include all required parameters in the request.
	•	All endpoints return JSON responses.
	•	Errors are returned in the format:

{
    "error": "Description of the error."
}



Feel free to check out the repository for the complete source code!
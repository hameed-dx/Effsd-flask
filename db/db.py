# Import the test data
from db.test_data import films_data

# Placeholder functions to simulate database operations

# Get all films
def get_all_films():
    return films_data

# Get a film by its ID
def get_film_by_id(film_id):
    return next((film for film in films_data if film['id'] == film_id), None)

import pytest

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User

class TestUserMethods:
    def test_init(self):
        user1 = User('Martin', 'pw12345')
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        print(user1)
        print(user2)
        print(user3)

        movie = Movie("Moana", 2016)
        director = Director("Ron Clements")
        movie.director = director
        movie.runtime_minutes = 104
        user1.watch_movie(movie)

        movie1 = Movie("Avengers", 2013)
        director1 = Director("Marvel")
        movie1.director = director1
        movie1.runtime_minutes = 124
        user1.watch_movie(movie1)

        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        user1.add_review(review)

        review_text1 = "Average movie"
        rating1 = 8
        review1 = Review(movie1, review_text1, rating1)
        user1.add_review(review1)
        print(user1.watched_movies)
        print(user1.time_spent_watching_movies_minutes)
        print(user1.reviews)
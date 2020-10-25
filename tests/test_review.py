import pytest

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie
from domainmodel.review import Review

class TestReviewMethods:
    def test(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)

        print(review.movie)
        print("Review: {}".format(review.review_text))
        print("Rating: {}".format(review.rating))

    def test_init(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)

        print(review.movie)
        print("Review: {}".format(review.review_text))
        print("Review: {}".format(review.timestamp))
        print("Rating: {}".format(review.rating))

    def test_eq(self):
        movie1 = Movie("Moana", 2016)
        review_text1 = "This movie was very enjoyable."
        rating1 = 8
        review1 = Review(movie1, review_text1, rating1)

        movie2 = Movie("Moana", 2016)
        review_text2 = "This movie was very enjoyable."
        rating2 = 8
        review2 = Review(movie2, review_text2, rating2)
        assert review1.__eq__(review2) == True
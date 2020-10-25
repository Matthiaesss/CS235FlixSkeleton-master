from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def __init__(self, movie, review_text, rating):
        self.__movie = movie
        self.__review_text = review_text
        if rating > 0 and rating < 11:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now()

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    @movie.setter
    def movie(self, movie: Movie):
        if isinstance(movie, Movie) is True:
            self.__movie = movie

    @review_text.setter
    def review_text(self, review_text):
        if type(review_text) is str:
            self.__review_text = review_text

    @rating.setter
    def rating(self, rating):
        if type(rating) is int:
            if rating > 0 and rating < 11:
                self.__rating = rating

    @timestamp.setter
    def timestamp(self, timestamp):
        if type(timestamp, datetime) is True:
            self.__timestamp = timestamp

    def __repr__(self):
        return f"<{self.__review_text}>"

    def __eq__(self, other):
        if self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp:
            return True
        else:
            return False


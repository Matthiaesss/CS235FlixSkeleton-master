from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, user_name, password):
        self.__user_name = user_name.strip().lower()
        self.__password = password
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @user_name.setter
    def user_name(self, user_name):
        if type(user_name) is str:
            self.__user_name = user_name.strip().lower()

    @password.setter
    def password(self, password):
        if type(password) is str:
            self.__password = password

    @watched_movies.setter
    def watched_movies(self, watched_movies):
        if isinstance(watched_movies, list) is True:
            self.__watched_movies = watched_movies

    @reviews.setter
    def reviews(self, reviews):
        if isinstance(reviews, list) is True:
            self.__reviews = reviews

    @time_spent_watching_movies_minutes.setter
    def time_spent_watched_movies_minutes(self, time_spent_watching_movies_minutes):
        if isinstance(time_spent_watching_movies_minutes, int) is True:
            self.__time_spent_watching_movies_minutes = time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if self.__user_name == other.__user_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__user_name[0] < other.__user_name[0]:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if isinstance(movie, Movie) is True:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review) is True:
            if review not in self.__reviews:
                self.__reviews.append(review)
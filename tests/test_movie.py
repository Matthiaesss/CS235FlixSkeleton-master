import pytest

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie

class TestMovieMethods:

    def test_init(self):
        movie1 = Movie("Moana", 2016)
        assert repr(movie1) == "<Movie Moana, 2016>"

    def test_title_year(self):
        movie1 = Movie("", "")
        print(movie1)
        movie2 = Movie(19, "yes")
        print(movie2)

    def test_description(self):
        movie1 = Movie("Moana", 2016)
        movie1.description = "Moana"
        movie1.description = 2016
        print(movie1.description)

    def test_director(self):
        movie1 = Movie("Moana", 2016)
        movie1.director = Director("Ron Clements")
        movie1.director = Director("Michael Bay")
        print(movie1.director)
        movie2 = Movie("Moana", 2016)
        movie2.director = "Ron Clements"
        print(movie2.director)

    def test_runtime(self):
        movie1 = Movie("Moana", 2016)
        movie1.runtime_minutes = "Moana"
        movie1.runtime_minutes = 107
        print(movie1.runtime_minutes)

    def test_eq(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Split", 2016)
        movie3 = Movie("Moana", 2016)
        assert movie1.__eq__(movie2) == False
        assert movie1.__eq__(movie3) == True

    def test_lt(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Split", 2016)
        movie3 = Movie("Moana", 1999)
        movie4 = Movie("", 2020)

        assert movie1.__lt__(movie2) == True
        assert movie1.__lt__(movie3) == False
        assert movie1.__lt__(movie4) == True
        assert movie4.__lt__(movie1) == False


    def test_hash(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Split", 2016)
        movie3 = Movie("Terminator", 2018)
        assert movie1.__hash__() == 9
        assert movie2.__hash__() == 9
        assert movie3.__hash__() == 14

    def test_add_actor(self):
        movie1 = Movie("Moana", 2016)
        movie1.add_actor(Actor("Auli'i Cravalho"))
        movie1.add_actor(Actor("Dwayne Johnson"))
        movie1.add_actor(Actor("Dwayne Johnson"))
        print(movie1.actors)


    def test_remove_actor(self):
        movie1 = Movie("Moana", 2016)
        movie1.add_actor(Actor("Auli'i Cravalho"))
        movie1.add_actor(Actor("Dwayne Johnson"))
        movie1.remove_actor(Actor("Auli'i Cravalho"))
        movie1.remove_actor(Actor("Angelina Jolie"))
        print(movie1.actors)


    def test_add_genre(self):
        movie1 = Movie("Moana", 2016)
        movie1.add_genre(Genre("Animation"))
        movie1.add_genre(Genre("Disney"))
        movie1.add_genre(Genre("Disney"))
        print(movie1.genres)


    def test_remove_genre(self):
        movie1 = Movie("Moana", 2016)
        movie1.add_genre(Genre("Animation"))
        movie1.add_genre(Genre("Disney"))
        movie1.remove_genre(Genre("Animation"))
        movie1.remove_genre(Genre("Kids"))
        print(movie1.genres)

    def test(self):
        movie = Movie("Moana", 2016)
        print(movie)

        director = Director("Ron Clements")
        movie.director = director
        print(movie.director)

        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        print(movie.actors)

        movie.runtime_minutes = 104
        print("Movie runtime: {} minutes".format(movie.runtime_minutes))

    def test_title(self):
        movie = Movie("Moana", 2016)
        print(movie.title)

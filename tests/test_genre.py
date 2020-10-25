import pytest

from domainmodel.genre import Genre

class TestGenreMethods:

    def test_init(self):
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(42)
        assert genre3.genre_name is None


    def test_eq(self):
        genre1 = Genre("Horror")
        genre2 = Genre("")
        genre3 = Genre(42)
        assert genre1.__eq__(genre2) == False
        assert genre2.__eq__(genre3) == True
        assert genre1.__eq__(genre3) == False


    def test_lt(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Action")
        genre3 = Genre("Comedy")
        assert genre2.__lt__(genre1) == True
        assert genre3.__lt__(genre1) == True
        assert genre2.__lt__(genre3) == True



    def test_hash(self):
        genre1 = Genre("Horror")
        genre2 = Genre("")
        genre3 = Genre(42)
        genre4 = Genre("Comedy")
        assert genre1.__hash__() == 6
        assert genre2.__hash__() == 0
        assert genre3.__hash__() == 0
        assert genre4.__hash__() == 6
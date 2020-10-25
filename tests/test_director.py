import pytest

from domainmodel.director import Director

class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None


    def test_eq(self):
        director1 = Director("Taika Waititi")
        director2 = Director("")
        director3 = Director(42)
        assert director1.__eq__(director2) == False
        assert director2.__eq__(director3) == True
        assert director1.__eq__(director3) == False

    def test_lt(self):
        director1 = Director("Cameron Diaz")
        director2 = Director("Angelina Jolie")
        director3 = Director("Brad Pitt")
        assert director2.__lt__(director1) == True
        assert director3.__lt__(director1) == True
        assert director2.__lt__(director3) == True



    def test_hash(self):
        director1 = Director("Taika Waititi")
        director2 = Director("")
        director3 = Director(42)
        director4 = Director("Tim Burton")
        assert director1.__hash__() == 13
        assert director2.__hash__() == 0
        assert director3.__hash__() == 0
        assert director4.__hash__() == 10
import pytest

from domainmodel.actor import Actor

class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None


    def test_eq(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("")
        actor3 = Actor(42)
        assert actor1.__eq__(actor2) == False
        assert actor2.__eq__(actor3) == True
        assert actor1.__eq__(actor3) == False


    def test_lt(self):
        actor1 = Actor("Cameron Diaz")
        actor2 = Actor("Angelina Jolie")
        actor3 = Actor("Brad Pitt")
        assert actor2.__lt__(actor1) == True
        assert actor3.__lt__(actor1) == True
        assert actor2.__lt__(actor3) == True



    def test_hash(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("")
        actor3 = Actor(42)
        actor4 = Actor("Brad Pitt")
        assert actor1.__hash__() == 14
        assert actor2.__hash__() == 0
        assert actor3.__hash__() == 0
        assert actor4.__hash__() == 9

    def test_add_actor_colleague(self):
        actor1 = Actor("Angelina Jolie")
        assert actor1.add_actor_colleague("Brad Pitt") == None

    def test_check_if_this_actor_worked_with(self):
        actor1 = Actor("Angelina Jolie")
        actor2 = Actor("Brad Pitt")
        actor3 = Actor("Cameron Diaz")
        actor1.add_actor_colleague(actor2)
        assert actor1.check_if_this_actor_worked_with(actor2) == True
        assert actor1.check_if_this_actor_worked_with(actor3) == False

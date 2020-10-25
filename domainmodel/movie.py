from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year == "" or type(release_year) is not int or release_year < 1900:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0


    @property
    def description(self):
        return self.__description

    @property
    def director(self):
        return self.__director

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @description.setter
    def description(self, description):
        if type(description) is str:
            if description == "":
                pass
            else:
                self.__description = description.strip()

    @director.setter
    def director(self, director: Director):
        if isinstance(director, Director) is True:
            if self.__director is None:
                self.__director = director

    @actors.setter
    def actors(self, actors):
        if isinstance(actors, list) is True:
            self.__actors = actors

    @genres.setter
    def genres(self, genres):
        if isinstance(genres, list) is True:
            self.__genres = genres

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is int:
            if runtime_minutes > 0:
                self.__runtime_minutes = runtime_minutes
            else:
                raise ValueError("Runtime must be positive")

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if self.__title == other.__title:
            if self.__release_year == other.__release_year:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.__title is None:
            return False
        elif other.__title is None:
            return True
        elif self.__title[0] == other.__title[0]:
            return self.__release_year < other.__release_year
        else:
            return self.__title[0] < other.__title[0]

    def __hash__(self):
        if self.__title is None:
            return 0
        elif self.__release_year is None:
            return hash(len(self.__title))
        else:
            return hash(len(self.__title) + len(str(self.__release_year)))

    def add_actor(self, actor: Actor):
        if isinstance(actor, Actor) is True:
            if actor not in self.__actors:
                self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if isinstance(actor, Actor) is True:
            if actor in self.__actors:
                self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        if isinstance(genre, Genre) is True:
            if genre not in self.__genres:
                self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if isinstance(genre, Genre) is True:
            if genre in self.__genres:
                self.__genres.remove(genre)

    def title(self):
        return self.__title

    def actors(self):
        return self.__actors

    def genres(self):
        return self.__genres

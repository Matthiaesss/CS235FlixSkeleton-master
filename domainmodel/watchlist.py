from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__movie_list = []
        self.__size = 0

    def add_movie(self, movie):
        if isinstance(movie, Movie) is True:
            if movie not in self.__movie_list:
                self.__movie_list.append(movie)
                self.__size += 1

    def remove_movie(self, movie):
        if isinstance(movie, Movie) is True:
            if movie in self.__movie_list:
                self.__movie_list.remove(movie)
                self.__size -= 1

    def select_movie_to_watch(self, index):
        if index > -1 and index < self.__size:
            return self.__movie_list[index]
        else:
            return None

    def size(self):
        return len(self.__movie_list)

    def first_movie_in_watchlist(self):
        if len(self.__movie_list) == 0:
            return None
        else:
            return self.__movie_list[0]

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        if self.__count < self.__size:
            movie = self.__movie_list[self.__count]
            self.__count += 1
            return movie
        else:
            raise StopIteration

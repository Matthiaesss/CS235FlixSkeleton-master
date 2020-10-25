import pytest

from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList

class TestWatchlistMethods:
    def test_first_movie(self):
        watchlist = WatchList()
        print(f"Size of watchlist: {watchlist.size()}")
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Split", 2016))
        watchlist.add_movie(Movie("Terminator", 1984))
        print(watchlist.first_movie_in_watchlist())

    def test_duplicate(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Split", 2016))
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Terminator", 1984))
        print(f"Size of watchlist: {watchlist.size()}")
        print(watchlist.first_movie_in_watchlist())


    def test_size(self):
        watchlist = WatchList()
        print(f"Size of watchlist: {watchlist.size()}")
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Split", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        watchlist.remove_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        print(watchlist.first_movie_in_watchlist())

    def test_remove_empty(self):
        watchlist = WatchList()
        print(f"Size of watchlist: {watchlist.size()}")
        watchlist.remove_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")

    def test_remove_add_first(self):
        watchlist = WatchList()
        print(f"Size of watchlist: {watchlist.size()}")
        watchlist.remove_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        print(watchlist.first_movie_in_watchlist())

    def test_select_movie(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        print(watchlist.select_movie_to_watch(0))
        print(watchlist.select_movie_to_watch(1))

    def test_iter_next(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Split", 2016))
        watchlist.__iter__()
        print(f"Next in watchlist: {watchlist.__next__()}")
        print(f"Next in watchlist: {watchlist.__next__()}")

    def test_first_movie_empty(self):
        watchlist = WatchList()
        print(f"Size of watchlist: {watchlist.size()}")
        print(watchlist.first_movie_in_watchlist())
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Split", 2016))
        watchlist.add_movie(Movie("Terminator", 1984))
        print(watchlist.first_movie_in_watchlist())

    def test_iter_end(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Split", 2016))
        watchlist.__iter__()
        print(f"Next in watchlist: {watchlist.__next__()}")
        print(f"Next in watchlist: {watchlist.__next__()}")
        print(f"Next in watchlist: {watchlist.__next__()}")
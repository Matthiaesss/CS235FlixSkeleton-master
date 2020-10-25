import pytest
import csv
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.movie import Movie

from datafilereaders.movie_file_csv_reader import MovieFileCSVReader

class TestMovieFileCSVReaderMethods:
    def test(self):
        filename = 'datafiles/Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()

        print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
        print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
        print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
        print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')

    def test_2(self):
        filename = 'datafiles/Data1000Movies.csv'
        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()

        all_directors_sorted = sorted(movie_file_reader.dataset_of_directors)
        print(all_directors_sorted)
        print(f'first 3 unique directors of sorted dataset: {all_directors_sorted[0:3]}')
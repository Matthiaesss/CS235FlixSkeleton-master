import pytest
import json
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from flask import Flask, redirect, url_for, render_template, request, session
from domainmodel.user import User
from domainmodel.review import Review
from domainmodel.movie import Movie
import csv
from csv import writer

from wsgi import main


def test_home():
    app = Flask(__name__)
    main(app)
    client = app.test_client()
    url = "/"
    response = client.get(url)
    assert response.status_code == 200


from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from flask import Flask, redirect, url_for, render_template, request, session
from domainmodel.user import User
from domainmodel.review import Review
from domainmodel.movie import Movie
import csv
from csv import writer

def main():
    app = Flask(__name__)
    app.secret_key = "key"
    x = False
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    count = 0
    movies = movie_file_reader.dataset_of_movies

    @app.route("/", methods = ["POST", "GET"])
    def homepage():
        return render_template("homepage.html")

    @app.route("/movies/", methods = ["POST", "GET"])
    def movies():
        global count
        global movies
        if request.method == "POST":
            if request.form.get("title_search") == "movie_search":
                search = request.form["movie_title"]
                movies = []
                count = 0
                for movie in movie_file_reader.dataset_of_movies:
                    if search.lower() in movie.title().lower():
                        movies.append(movie)
                if len(movies) == 0:
                    return render_template("movies.html", title="Movie not found")
                return render_template("movies.html", title = "Movie: {}".format(movies[count].title()),
                                               director = "Director: {}".format(movies[count].director.director_full_name),
                                               genre = "Genre: {}".format(movies[count].genres()),
                                               actors = "Actors: {}".format(movies[count].actors()),
                                               desc = "Description: {}".format(movies[count].description))

        if request.method == "POST":
            if request.form.get("previous_btn") == "minus":
                try:
                    if count > 0:
                        count -= 1
                except NameError:
                    return render_template("movies.html")

                return render_template("movies.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            elif request.form.get("next_btn") == "plus":
                try:
                    if count < len(movies) - 1:
                        count += 1
                except NameError:
                    return render_template("movies.html")

                return render_template("movies.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            return render_template("movies.html", title="Movie: {}".format(movies[count].title()),
                                   director="Director: {}".format(movies[count].director.director_full_name),
                                   genre="Genre: {}".format(movies[count].genres()),
                                   actors="Actors: {}".format(movies[count].actors()),
                                   desc="Description: {}".format(movies[count].description))

        else:
            return render_template("movies.html")




    @app.route("/actors/", methods = ["POST", "GET"])
    def actors():
        global count
        global movies
        if request.method == "POST":
            if request.form.get("name_search") == "actor_search":
                search = request.form["a_s"]
                for actor_name in movie_file_reader.dataset_of_actors:
                    if actor_name.actor_full_name.lower() == search.lower():
                        movies = []
                        for movie in movie_file_reader.dataset_of_movies:
                            if actor_name in movie.actors():
                                movies.append(movie)
                        count = 0
                        return render_template("actors.html", title="Movie: {}".format(movies[count].title()),
                                               director="Director: {}".format(movies[count].director.director_full_name),
                                               genre="Genre: {}".format(movies[count].genres()),
                                               actors="Actors: {}".format(movies[count].actors()),
                                               desc="Description: {}".format(movies[count].description))

                return render_template("actors.html", title = "Actor not found")
        else:
            return render_template("actors.html")

        if request.method == "POST":
            if request.form.get("previous_btn") == "minus":
                try:
                    if count > 0:
                        count -= 1
                except NameError:
                    return render_template("actors.html")

                return render_template("actors.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            elif request.form.get("next_btn") == "plus":
                try:
                    if count < len(movies) - 1:
                        count += 1
                except NameError:
                    return render_template("actors.html")

                return render_template("actors.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            return render_template("actors.html", title="Movie: {}".format(movies[count].title()),
                                   director="Director: {}".format(movies[count].director.director_full_name),
                                   genre="Genre: {}".format(movies[count].genres()),
                                   actors="Actors: {}".format(movies[count].actors()),
                                   desc="Description: {}".format(movies[count].description))

    @app.route("/genres/", methods = ["POST", "GET"])
    def genres():
        global count
        global movies
        if request.method == "POST":
            if request.form.get("name_genre") == "genre_search":
                search = request.form["g_s"]
                for g in movie_file_reader.dataset_of_genres:
                    if g.genre_name.lower() == search.lower():
                        movies = []
                        for movie in movie_file_reader.dataset_of_movies:
                            if g in movie.genres():
                                movies.append(movie)
                        count = 0
                        return render_template("genres.html", title="Movie: {}".format(movies[count].title()),
                                               director="Director: {}".format(movies[count].director.director_full_name),
                                               genre="Genre: {}".format(movies[count].genres()),
                                               actors="Actors: {}".format(movies[count].actors()),
                                               desc="Description: {}".format(movies[count].description))

                return render_template("genres.html", title="Genre not found")
        else:
            return render_template("genres.html")

        if request.method == "POST":
            if request.form.get("previous_btn") == "minus":
                try:
                    if count > 0:
                        count -= 1
                except NameError:
                    return render_template("movies.html")

                return render_template("genres.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            elif request.form.get("next_btn") == "plus":
                try:
                    if count < len(movies) - 1:
                        count += 1
                except NameError:
                    return render_template("genres.html")

                return render_template("genres.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            return render_template("genres.html", title="Movie: {}".format(movies[count].title()),
                                   director="Director: {}".format(movies[count].director.director_full_name),
                                   genre="Genre: {}".format(movies[count].genres()),
                                   actors="Actors: {}".format(movies[count].actors()),
                                   desc="Description: {}".format(movies[count].description))

    @app.route("/directors/", methods = ["POST", "GET"])
    def directors():
        global count
        global movies
        if request.method == "POST":
            if request.form.get("name_director") == "director_search":
                search = request.form["d_s"]
                for d in movie_file_reader.dataset_of_directors:
                    if d.director_full_name.lower() == search.lower():
                        movies = []
                        for movie in movie_file_reader.dataset_of_movies:
                            if d == movie.director:
                                movies.append(movie)
                        count = 0
                        return render_template("directors.html", title="Movie: {}".format(movies[count].title()),
                                               director="Director: {}".format(
                                                   movies[count].director.director_full_name),
                                               genre="Genre: {}".format(movies[count].genres()),
                                               actors="Actors: {}".format(movies[count].actors()),
                                               desc="Description: {}".format(movies[count].description))

                return render_template("directors.html", title="Director not found")
        else:
            return render_template("directors.html")

        if request.method == "POST":
            if request.form.get("previous_btn") == "minus":
                try:
                    if count > 0:
                        count -= 1
                except NameError:
                    return render_template("directors.html")

                return render_template("directors.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            elif request.form.get("next_btn") == "plus":
                try:
                    if count < len(movies) - 1:
                        count += 1
                except NameError:
                    return render_template("directors.html")

                return render_template("directors.html", title="Movie: {}".format(movies[count].title()),
                                       director="Director: {}".format(movies[count].director.director_full_name),
                                       genre="Genre: {}".format(movies[count].genres()),
                                       actors="Actors: {}".format(movies[count].actors()),
                                       desc="Description: {}".format(movies[count].description))

            return render_template("directors.html", title="Movie: {}".format(movies[count].title()),
                                   director="Director: {}".format(movies[count].director.director_full_name),
                                   genre="Genre: {}".format(movies[count].genres()),
                                   actors="Actors: {}".format(movies[count].actors()),
                                   desc="Description: {}".format(movies[count].description))

    @app.route("/register/", methods = ["POST", "GET"])
    def register():
        if request.method == "POST":
            if request.form.get("submit_button") == "submit_btn":
                user = request.form["user"]
                password = request.form["password"]
                if user == "" or password == "":
                    return render_template("register.html", error_message="Username or Password cannot be empty")
                else:
                    user_object = User(user, password)
                    with open('datafiles/users.csv', "a", newline="") as write_object:
                        with open('datafiles/users.csv', 'r') as reading:
                            readfile = csv.reader(reading)
                            for row in readfile:
                                if row[0] == user:
                                    return render_template("register.html", error_message="Username already taken")
                        csv_writer = writer(write_object)
                        csv_writer.writerow([user, password])
                    return render_template("login.html")
        else:
            return render_template("register.html")

    @app.route("/login/", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            if request.form.get("login_button") == "login_btn":
                user = request.form["user"]
                password = request.form["password"]
                if user == "" or password == "":
                    return render_template("login.html", error_message="Username or Password cannot be empty")
                else:
                    with open('datafiles/users.csv', "r") as write_object:
                        readfile = csv.reader(write_object)
                        for row in readfile:
                            if row[0] == user and row[1] == password:
                                session["user"] = user
                                return render_template("reviews.html")
                    return render_template("login.html")
        else:
            if "user" in session:
                return render_template("reviews.html")
            return render_template("login.html")

    @app.route("/reviews/", methods=["POST", "GET"])
    def reviews():
        if "user" in session:
            user_session = session["user"]
            if request.method == "POST":
                if request.form.get("logout_button") == "logout_btn":
                    session.pop("user", None)
                    return render_template("login.html", error_message="You have logged out")
                if request.form.get("submit_button") == "submit_btn":
                    title = request.form.get("title")
                    rating = request.form.get("rating")
                    review = request.form.get("review")
                    user_review = Review(title, rating, review)
        else:
            return render_template("login.html")

    app.run(debug=True)

main()
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/movies/", methods = ["POST", "GET"])
def movies():
    return render_template("movies.html")

@app.route("/actors/")
def actors():
    return render_template("actors.html")

@app.route("/genres/")
def genres():
    return render_template("genres.html")

@app.route("/directors/")
def directors():
    return render_template("directors.html")


if __name__ == "__main__":
    app.run(debug = True)


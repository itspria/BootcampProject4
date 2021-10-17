# import necessary libraries
#from models import create_classes
import initdb

import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search/<movieName>")
def recommend(movieName):
    print("Collecting recommendations for the movie: ", movieName)

    results1 = initdb.GetMoviesByUserRating(movieName)
    results2 = initdb.GetMoviesByGenre(movieName)
    results3 = initdb.GetMoviesByDescription(movieName)
    
    return render_template("index.html", listings1=results1, listings2=results2, listings3=results3)

@app.route("/rating")
def chart1():
    return render_template("highestrating.html")

@app.route("/duration")
def chart2():
    return render_template("duration.html")

@app.route("/genre")
def chart3():
    return render_template("rating.html")

if __name__ == "__main__":
    app.run()

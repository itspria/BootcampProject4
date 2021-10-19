# import necessary libraries
#from models import create_classes
import initdb
import pandas as pd
import numpy
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
    predict = initdb.GetPredictionsForMovie(movieName)
    predictions = []
    for key,value in predict.items():
        txt = f'{key}: {value}'
        predictions.append(txt)
    
    return render_template("index.html", listings1=results1, listings2=results2, listings3=results3, movie="for " + movieName, predictions=predictions)

#@app.route("/search/<movieName>/<userid>")
@app.route("/usersearch", methods=['GET'])
def recommendwithuser():
    movieName = request.args.get('movieName', None) # use default value repalce 'None'
    userid = request.args.get('userid', None)

    print(f"Collecting recommendations for the movie: {movieName} and user: {userid}")

    results1 = initdb.GetMoviesByUserRating(movieName)
    results2 = initdb.GetMoviesByGenre(movieName)
    results3 = initdb.GetMoviesByDescription(movieName)

    predict = initdb.GetPredictions(movieName, userid)
    displaytxt = f"for {movieName} and user {userid}"
    predictions = []
    for key,value in predict.items():
        txt = f'{key}: {value}'
        predictions.append(txt)

    return render_template("index.html", listings1=results1, listings2=results2, listings3=results3, movie=displaytxt, predictions=predictions)

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


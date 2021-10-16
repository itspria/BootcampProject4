import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def GetMoviesByDescription(movieName):
    movie_list=[]
    return movie_list

def GetMoviesByUserRating(movieName):
    movies = pd.read_csv("raw data/movies.csv")
    ratings = pd.read_csv("raw data/ratings.csv")
    movievsuser = ratings.pivot(index='movieId',columns='userId',values='rating')
    movievsuser.fillna(0, inplace=True)
    ratingsByMovie = ratings.groupby('movieId')['rating'].agg('count')
    ratingsByUser = ratings.groupby('userId')['rating'].agg('count')
    movievsuser = movievsuser.loc[ratingsByMovie[ratingsByMovie > 40].index,:]
    csr_data = csr_matrix(movievsuser.values)
    movievsuser.reset_index(inplace=True)

    # Using KNN algorithm to predict similarity with cosine distance
    knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
    knn.fit(csr_data)     

    reccomendCount = 8
    movieList = movies[movies['title'].str.contains(movieName)]  
    if len(movieList):        
        movie_id= movieList.iloc[0]['movieId']
        movie_id = movievsuser[movievsuser['movieId'] == movie_id].index[0]
        distances , indices = knn.kneighbors(csr_data[movie_id],n_neighbors=reccomendCount+1)    
        recommendedMovies = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
        recMoviesList = []
        for val in recommendedMovies:
            movie_id = movievsuser.iloc[val[0]]['movieId']
            idx = movies[movies['movieId'] == movie_id].index
            recMoviesList.append({'Title':movies.iloc[idx]['title'].values[0],'Distance':val[1]})
        df = pd.DataFrame(recMoviesList,index=range(1,reccomendCount+1))
        df['Distance'] = pd.to_numeric(df['Distance'])
        df= df.sort_values('Distance')
    
    listing = df['Title']
    return listing

def GetMoviesByGenre(movieName):
    file_to_load = "raw data/movies.csv"
    ratings = pd.read_csv("raw data/ratings.csv")

    data = pd.read_csv(file_to_load)
    data['genres'] = data['genres'].str.replace(r'|', ' ')
    genre_data=data[['title','genres']]
    genre_data=genre_data.set_index('title')
    
    #convert genre column to array
    cv = CountVectorizer()
    X = cv.fit_transform(genre_data["genres"]).toarray()

    similarities = cosine_similarity(X)
    movie_index = data.loc[data['title'].str.contains(movieName)].index[0]
    
    similarity_values = pd.Series(similarities[movie_index])

    #We converted list into series in order to preserve the actual indexes of dataset even after sorting
    similarity_values.sort_values(ascending=False)
    similar_movie_indexes = list(similarity_values.sort_values(ascending=False).index)

    #Remove the already watched movie from index list
    similar_movie_indexes.remove(movie_index)

    movie_list=[]
    for i in range(10):
        movie_list.append(genre_data.index[similar_movie_indexes[i]])

    return movie_list




# Movie Recommender
### Project Outline
A Recommender System refers to a system that is capable of predicting the future preference of a set of items for a user, and recommend the top items.

Recommender systems attempt to solve the problem of information overload along with providing personalizations that help users make optimized decisions.

#### Data Extraction
The datasets used in this projects are from IMDB and MovieLens
- https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset
- https://grouplens.org/datasets/movielens/latest/
 
#### Data Visualization 
Tableau was used for preparing visualizations

#### Model Creation
- Content Based Filtering (get movie recommendations)
  - Using Genre
  - Using Movie Description

- Unsupervised Learning (get movie recommendations)
 KNN Movie Recommender

- Supervised Learning (get predicted movie rating)
  - Singular Value Decomposition Matrix Factorization (SVD MF); using surprise python scikit
  - XGBoost Algorithm (XGBoost is an implementation of gradient boosted decision trees designed for speed and performance)
  
#### Model Optimization
- SVD MF
  The starting RMSE for SVD MF was 0.65, and MAE is 0.50. With optimization we were able to reduce it RMSE to 0.28 and MAE to 0.18.
- XGBoost
  The starting RMSE for XGBoost was 0.68, and MAPE is 20.6. With optimization we were able to reduce it RMSE to 0.63 and MAPE to 18.7.
  
#### Deployment to the Web
  https://movie-recommender-2021.herokuapp.com/

![Homescreen](https://github.com/itspria/BootcampProject1/blob/main/images/home.PNG)

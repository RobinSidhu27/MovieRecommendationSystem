import numpy as np
import pandas as pd
import ast

def load_and_clean_data():
  
  def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
      L.append(i['name'])
    return L

  def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
      if counter != 3:
        L.append(i['name'])
        counter += 1
      else:
        break
    return L

  def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
      if i['job'] == 'Director':
        L.append(i['name'])
        break
    return L

  movies = pd.read_csv('/Users/robinsidhu/Robin/Projects/Movie_Reco/archive/tmdb_5000_movies.csv')
  credits = pd.read_csv('/Users/robinsidhu/Robin/Projects/Movie_Reco/archive/tmdb_5000_credits.csv')

  movies = movies.merge(credits, on='title')

  movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

  movies['genres'] = movies['genres'].apply(convert)
  movies['keywords'] = movies['keywords'].apply(convert)
  movies['cast'] = movies['cast'].apply(convert3)
  movies['crew'] = movies['crew'].apply(fetch_director)
  movies['overview'] = movies['overview'].fillna('').apply(lambda x:x.split())

  movies['genres'].apply(lambda x:[i.replace(" ", "") for i in x])
  movies['keywords'].apply(lambda x:[i.replace(" ", "") for i in x])
  movies['crew'].apply(lambda x:[i.replace(" ", "") for i in x])
  movies['overview'].apply(lambda x:[i.replace(" ", "") for i in x])

  movies['tags'] = movies['genres'] + movies['crew'] + movies['overview'] + movies['cast'] + movies['keywords']

  newdf = movies[['movie_id', 'title', 'tags']]
  newdf['tags'] = newdf['tags'].apply(lambda x:" ".join(x))

  return newdf

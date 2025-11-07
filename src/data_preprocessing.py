import numpy as np
import pandas as pd
import ast
import os

def load_and_clean_data():

    # --------------------------
    # Helper functions
    # --------------------------
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
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return [i['name']]
        return []

    # --------------------------
    # Correct file paths (Render compatible)
    # --------------------------
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "..", "archive")

    movies_path = os.path.join(DATA_DIR, "tmdb_5000_movies.csv")
    credits_path = os.path.join(DATA_DIR, "tmdb_5000_credits.csv")

    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    # --------------------------
    # Merge and filter columns
    # --------------------------
    movies = movies.merge(credits, on='title')

    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

    # --------------------------
    # Apply transformations
    # --------------------------
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert3)
    movies['crew'] = movies['crew'].apply(fetch_director)
    movies['overview'] = movies['overview'].fillna('').apply(lambda x: x.split())

    # Actually REPLACE spaces inside items
    movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['overview'] = movies['overview'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])

    # --------------------------
    # Build final tags
    # --------------------------
    movies['tags'] = movies['genres'] + movies['crew'] + movies['overview'] + movies['cast'] + movies['keywords']

    newdf = movies[['movie_id', 'title', 'tags']].copy()
    newdf['tags'] = newdf['tags'].apply(lambda x: " ".join(x))

    return newdf

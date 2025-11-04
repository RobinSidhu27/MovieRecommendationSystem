# src/main.py
from data_preprocessing import load_and_clean_data
from vectorization import vectorize_data
import numpy as np

def recommend(movie_name, movies, similarity):
    movie_index = movies[movies['title'].str.lower() == movie_name.lower()].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    print("\nTop 5 recommendations:")
    for i in movie_list:
        print(movies.iloc[i[0]].title)

def main():
    print("Loading data...")
    movies = load_and_clean_data()
    print("Vectorizing data...")
    similarity, _ = vectorize_data(movies)

    movie_name = input("Enter a movie name: ")
    recommend(movie_name, movies, similarity)

if __name__ == "__main__":
    main()

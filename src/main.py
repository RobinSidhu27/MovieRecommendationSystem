from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie_name, movies, vectors):
    # Get index of movie
    movie_index = movies[movies['title'].str.lower() == movie_name.lower()].index[0]

    # Vector for this movie
    movie_vector = vectors[movie_index]

    # Compute similarity ON DEMAND
    similarity_scores = cosine_similarity(movie_vector, vectors).flatten()

    # Sort and pick top 5 recommendations
    movie_list = sorted(
        list(enumerate(similarity_scores)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]
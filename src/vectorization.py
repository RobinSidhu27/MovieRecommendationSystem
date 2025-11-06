# src/vectorization.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.data_preprocessing import load_and_clean_data


def vectorize_data(movies_df):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies_df['tags']).toarray()

    similarity = cosine_similarity(vectors)
    return similarity, cv

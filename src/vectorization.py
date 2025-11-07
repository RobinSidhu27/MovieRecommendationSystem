# src/vectorization.py
from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_data(movies):
    tfidf = TfidfVectorizer(stop_words='english', max_features=10000)
    vectors = tfidf.fit_transform(movies['tags'])
    return vectors, tfidf


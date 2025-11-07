from src.data_preprocessing import load_and_clean_data
from src.vectorization import vectorize_data
import joblib

movies = load_and_clean_data()
similarity, vectorizes = vectorize_data(movies)

joblib.dump(movies, "movies.pkl")
joblib.dump(similarity, "similarity.pkl")

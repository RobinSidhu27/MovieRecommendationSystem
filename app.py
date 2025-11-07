from flask import Flask, render_template, request, jsonify
from src.main import recommend
from src.data_preprocessing import load_and_clean_data
from src.vectorization import vectorize_data
import joblib


app = Flask(__name__)

movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity.pkl")


@app.route("/")
def home():
    return render_template("index.html")

def get_poster_path(index):
    try:
        return movies.iloc[index]['poster_path']
    except:
        return None


@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data = request.get_json()
    movie = data.get("movie", "").strip()

    if not movie:
        return jsonify({"error": "Please enter a movie name.", "results": []})

    # Check if the movie exists in the dataset
    titles_lower = movies['title'].str.lower().tolist()
    if movie.lower() not in titles_lower:
        return jsonify({"error": f"No movie found with the name '{movie}'.", "results": []})

    try:
        raw_results = recommend(movie, movies, similarity)
        results = []
        for title in raw_results:
            idx = movies[movies['title'] == title].index[0]
            poster = movies.iloc[idx]['poster_path'] if 'poster_path' in movies.columns else None

            # TMDB full poster URL
            if poster:
                poster_url = f"https://image.tmdb.org/t/p/w500{poster}"
            else:
                poster_url = None

            results.append({
                "title": title,
                "poster": poster_url
            })

        return jsonify({"error": None, "results": results})

    except Exception as e:
        print("Backend error:", e)
        return jsonify({"error": "Something went wrong. Try another title.", "results": []})


@app.route("/movies")
def get_movies():
    titles = movies['title'].tolist()
    return jsonify(titles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


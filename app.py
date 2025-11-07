from flask import Flask, render_template, request, jsonify
import joblib
from src.vectorization import vectorize_data
from src.main import recommend

app = Flask(__name__)

# -----------------------------
# Load precomputed movies data
# -----------------------------
print("Loading movies.pkl...")
movies = joblib.load("movies.pkl")

# -----------------------------
# Build TF-IDF matrix only (lightweight)
# -----------------------------
print("Vectorizing tags...")
vectors, vectorizer = vectorize_data(movies)

print("✅ Backend ready.")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data = request.get_json()
    movie = data.get("movie", "").strip()

    if not movie:
        return jsonify({"error": "Please enter a movie name.", "results": []})

    titles_lower = movies['title'].str.lower().tolist()
    if movie.lower() not in titles_lower:
        return jsonify({"error": f"No movie found with the name '{movie}'.", "results": []})

    try:
        rec_titles = recommend(movie, movies, vectors)
        results = []

        for title in rec_titles:
            idx = movies[movies['title'] == title].index[0]

            poster = None
            if "poster_path" in movies.columns:
                raw = movies.iloc[idx].get("poster_path", None)
                if isinstance(raw, str) and raw.strip():
                    poster = f"https://image.tmdb.org/t/p/w500{raw}"

            results.append({
                "title": title,
                "poster": poster
            })

        return jsonify({"error": None, "results": results})

    except Exception as e:
        print("Backend error:", e)
        return jsonify({"error": "Server error. Try again.", "results": []})


@app.route("/movies")
def get_movies():
    return jsonify(movies['title'].tolist())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

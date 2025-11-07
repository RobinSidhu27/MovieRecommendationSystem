from flask import Flask, render_template, request, jsonify
from src.vectorization import vectorize_data
from src.main import recommend
import joblib

app = Flask(__name__)

# -----------------------------
# Load precomputed movies dataframe
# -----------------------------
print("Loading movies.pkl...")
movies = joblib.load("movies.pkl")

# -----------------------------
# Compute similarity (safe for Render)
# -----------------------------
print("Generating similarity matrix...")
similarity, _ = vectorize_data(movies)

print("✅ Server ready.")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data = request.get_json()
    movie = data.get("movie", "").strip()

    if not movie:
        return jsonify({"error": "Please enter a movie name.", "results": []})

    # Validate movie name
    titles_lower = movies['title'].str.lower().tolist()
    if movie.lower() not in titles_lower:
        return jsonify({"error": f"No movie found with the name '{movie}'.", "results": []})

    try:
        result_titles = recommend(movie, movies, similarity)
        results = []

        for title in result_titles:
            idx = movies[movies['title'] == title].index[0]

            poster = None
            if "poster_path" in movies.columns:
                path = movies.iloc[idx]["poster_path"]
                if isinstance(path, str) and path.strip():
                    poster = f"https://image.tmdb.org/t/p/w500{path}"

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

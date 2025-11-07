# 🎬 Movie Recommendation System
### Live Demo
https://movierecommendationsystem-cgca.onrender.com/

A lightweight, modern, ML-powered movie recommendation web app built using **Flask**, **TF-IDF vectorization**, and a polished glassmorphic UI.

This version is optimized for **Render free tier**, using **on-demand similarity computation** to prevent huge memory usage and deployment crashes.

---

## ✅ Features

### 🔍 Smart Recommendations
- Finds 5 similar movies using **TF-IDF + cosine similarity**
- Accurate, fast, no heavy precomputed matrices
- Works smoothly even on limited RAM environments like Render free tier

### ⚡ Lightweight Backend
- No large `.pkl` similarity files
- No 200MB+ RAM spikes
- Instant startup time
- Fully cloud-friendly

### ✨ Modern UI
- Apple-style glassmorphism
- Autocomplete movie suggestions
- Skeleton shimmer loaders
- TMDB poster fetching
- Smooth animations
- Dark mode support

### 🚀 Deployment Ready
- Gunicorn server
- Render deployment
- UptimeRobot keep-alive compatible

---

## ✅ Tech Stack

**Backend**  
- Python  
- Flask  
- Scikit-learn  
- TF-IDF Vectorizer  

**Frontend**  
- HTML + CSS + JavaScript  
- Dark/light UI  
- Animated components  

**DevOps / Deployment**  
- Render Web Service  
- Gunicorn  
- UptimeRobot monitor

---

## ✅ How It Works

### 1. Preprocessing  
`data_preprocessing.py` loads & cleans the dataset:  
- Extracts genres, cast, keywords  
- Removes spaces  
- Builds a combined **tags** field containing all metadata  

### 2. Vectorization  
`vectorization.py` applies TF-IDF:

```python
tfidf = TfidfVectorizer(stop_words='english', max_features=10000)
vectors = tfidf.fit_transform(movies['tags'])
```

### 3. On-Demand Recommendations

- Instead of generating a 176MB similarity matrix, the system computes:
- cosine_similarity(movie_vec, vectors).flatten()


### 4. Run locally
git clone https://github.com/RobinSidhu27/MovieRecommendationSystem.git
cd MovieRecommendationSystem
pip install -r requirements.txt
python app.py

- then visit
http://localhost:5000

### ✅ Deploying on Render
- Build Command
pip install -r requirements.txt

- Start Command
gunicorn app:app

Add an UptimeRobot monitor to prevent automatic sleeping.

### ✅ Dataset Source
TMDB 5000 Dataset
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

### ✅ Future Enhancements
- Movie trailers via YouTube API
- User ratings
- Collaborative filtering
- Theme personalization
- Docker deployment + CI/CD pipeline

### ✅ Author
Shehbaz Singh Sidhu
B.E. Computer Engineering
Thapar Institute of Engineering and Technology

### ✅ License
MIT License
Feel free to use, modify, and share.
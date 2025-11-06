# 🎬 Movie Recommendation System  
A lightweight, fast, and interactive movie recommendation system built using Python, Flask, and machine learning.  
The UI is fully modernized with glassmorphism, Spotlight-style search animation, VisionOS depth blur, and smooth iOS-style scroll physics.

---

## ✅ Features

### 🔍 Smart Movie Search  
- Auto-complete suggestions as you type  
- Spotlight-style expanding search bar  
- Real-time validation for unknown titles

### 🎥 Recommendations  
- Content-based filtering  
- Top-5 similar movie predictions  
- Uses TF-IDF vectorization + cosine similarity  
- Includes movie posters (from TMDB paths)

### ⚡ UI Enhancements  
- Skeleton loading animation  
- Glassmorphic floating navbar  
- VisionOS depth-blur behind cards  
- Hover-based micro-interactions  
- Fully responsive light/dark mode

---

## ✅ Tech Stack

**Backend**
- Python
- Flask
- Pandas
- Scikit-Learn (TF-IDF, Cosine Similarity)

**Frontend**
- HTML, CSS, JavaScript
- Dynamic fetch API calls
- Custom animations (CSS + JS)

---

## ✅ Project Structure


---

## ✅ How It Works

1. **Load & Clean Data**  
   `data_preprocessing.py` extracts and merges dataset fields like genres, cast, crew, and keywords into a unified `tags` column.

2. **Vectorize Movie Data**  
   `vectorization.py` applies TF-IDF vectorization on preprocessed tags and computes **cosine similarity** between all movies.

3. **Recommend Movies**  
   `main.py` contains the `recommend()` function that returns the Top-5 most similar titles.

4. **Serve UI with Flask**  
   `app.py` loads models once on startup and exposes two endpoints:
   - `/movies` — returns all movie titles for autocomplete
   - `/recommend` — returns recommendations + posters

---

## ✅ Running the Project

### **1. Install Dependencies**
```bash
pip install -r requirements.txt

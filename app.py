# app.py

import streamlit as st
from PIL import Image
from deepface import DeepFace
import random
import tempfile
import json
import requests
from dotenv import load_dotenv
import os

st.title("🎬 Mood to Movie Recommender 🎭")

load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Load your movies from the JSON file
try:
    with open("movie.json", "r", encoding="utf-8") as f:
        mood_to_movies = json.load(f)
except FileNotFoundError:
    st.error("❗ Could not find 'movie.json'. Please make sure the file exists in the same directory as this app.")
    st.stop()

uploaded_file = st.file_uploader("Upload your selfie:", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Selfie", use_container_width=True)
    try:
        # Save the uploaded image to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            temp_image_path = tmp_file.name

        result = DeepFace.analyze(img_path=temp_image_path, actions=['emotion'], enforce_detection=False)
        mood = result[0]['dominant_emotion']
        st.success(f"Your mood is detected as: **{mood.capitalize()}**")

        mood_lower = mood.lower()
        movies_list = mood_to_movies.get(mood_lower, mood_to_movies.get("neutral", []))
        
        if not movies_list:
            st.warning("No movies found for this mood.")
        else:
            chosen_movie = random.choice(movies_list)
            title = chosen_movie["title"]
            link = chosen_movie["imdb_link"]

            st.markdown("## 🎥 Recommended Movie:")
            st.markdown(f"- [{title}]({link})")
    except Exception as e:
        st.error(f"❗ Error in emotion detection: {str(e)}")

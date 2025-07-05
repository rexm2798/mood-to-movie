import os
import json
import random
import requests
import streamlit as st
from PIL import Image
from deepface import DeepFace
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Load the mood-to-movie mapping from JSON
with open("movie.json", "r", encoding="utf-8") as f:
    mood_to_movies = json.load(f)

def fetch_movie_details(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
        else:
            st.warning(f"No details found for {title}.")
            return None
    else:
        st.error("Failed to fetch movie details.")
        return None

def detect_mood_and_recommend(image_path):
    if image_path:
        try:
            img = Image.open(image_path)
            # st.image(img, caption="Your Selfie", use_container_width=True)

            result = DeepFace.analyze(
                img_path=image_path,
                actions=['emotion'],
                enforce_detection=False
            )

            mood = result[0]['dominant_emotion']
            st.success(f"Your mood is detected as: **{mood.capitalize()}**")

            mood_lower = mood.lower()
            movies_list = mood_to_movies.get(mood_lower, mood_to_movies["neutral"])
            chosen_movie = random.choice(movies_list)
            title = chosen_movie["title"]
            imdb_link = chosen_movie["imdb_link"]

            if OMDB_API_KEY:
                movie_data = fetch_movie_details(title, OMDB_API_KEY)
                if movie_data:
                    display_movie_details(movie_data)
                else:
                    fallback_display(title, imdb_link)
            else:
                fallback_display(title, imdb_link)

        except Exception as e:
            st.error(f"Error in emotion detection: {str(e)}")
    else:
        st.warning("No image path provided for mood detection.")

def display_movie_details(movie_data):
    st.markdown("## 🎥 Recommended Movie Details")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(movie_data["Poster"], caption=movie_data["Title"], use_container_width=True)
    
    with col2:
        st.markdown(f"### [{movie_data['Title']}](https://www.imdb.com/title/{movie_data['imdbID']}) ({movie_data['Year']})")
        st.markdown(f"**IMDB Rating**: ⭐ {movie_data['imdbRating']}/10")
        st.markdown(f"**Genre**: {movie_data['Genre']}")
        st.markdown(f"**Plot**: {movie_data['Plot']}")

def fallback_display(title, imdb_link):
    st.markdown("## 🎥 Recommended Movie (Basic):")
    st.markdown(f"- [{title}]({imdb_link})")

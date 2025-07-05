import streamlit as st
from movie_recommender import detect_mood_and_recommend

st.title("🎬 Mood to Movie Recommender 🎭")

uploaded_file = st.file_uploader("Upload your selfie:", type=["jpg", "png"])

detect_mood_and_recommend(uploaded_file)
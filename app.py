import streamlit as st
from PIL import Image
import tempfile
from movie_recommender import detect_mood_and_recommend

st.title("🎬 Mood to Movie Recommender 🎭")

# Allow user to take a selfie or upload an image
camera_image = st.camera_input("Take a selfie 📸")
uploaded_file = st.file_uploader("Or upload your selfie:", type=["jpg", "png"])

# Use camera input if available; otherwise use uploaded file
image_data = camera_image or uploaded_file

if image_data:
    # Display the captured or uploaded image
    img = Image.open(image_data)
    st.image(img, caption="Your Selfie", use_container_width=True)

    # Save image to a temporary file for processing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(image_data.getbuffer())
        temp_image_path = tmp_file.name

    # Detect mood and recommend a movie
    detect_mood_and_recommend(temp_image_path)
